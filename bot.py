import aiohttp
import asyncio

import json
import discord

import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")

API_URL = "http://localhost:8000/v1/chat/completions"
headers = {"Content-Type": "application/json"}


payload = {
    "max_token" : 512,
    "messages": []
}

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!carl'):
            stripped_message = str(message.content).replace('!ai', '').strip()
            prompt_message = {
                "role": "user",
                "content": f"{stripped_message} ### Responese: " 
            }
            payload["messages"].append(prompt_message)
            async with aiohttp.ClientSession() as session:
                async with session.post(API_URL, data=json.dumps(payload), headers=headers) as resp:

                    reply = await resp.json()
                    reply_content = reply["choices"][0]["message"]["content"]
                    print(f"Bot :{reply_content}")
                    await message.reply(reply_content, mention_author=True)

            msg_index = payload["messages"].index(prompt_message) 
            payload["messages"][msg_index]["content"] += reply_content

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)