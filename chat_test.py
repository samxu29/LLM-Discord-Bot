import aiohttp
import asyncio

import json

API_URL = "http://localhost:8000/v1/chat/completions"
headers = {"Content-Type": "application/json"}

# payload = {
#     "max_token" : 512,
#     "messages": [
#         {
#             "role": "user",
#             "content": "How is city of Charlotte in North Carolina? ### Response: "
#         }
#     ]
# }

payload = {
    "max_token" : 512,
    "messages": []
}

async def main():
    while True:
        prompt = input("User: ")
        
        message = {
            "role": "user",
            "content": f"{prompt} ### Responese: " 
        }
        # payload = {
        #     "max_token" : 512,
        #     "messages": [
        #         {
        #             "role": "user",
        #             "content": f"{prompt} ### Response: "
        #         }
        #     ]
        # }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(API_URL, data=json.dumps(payload), headers=headers) as resp:

                reply = await resp.json()
                reply_content = reply["choices"][0]["message"]["content"]
                # print(resp.status)
                # print(await resp.text())
                print(f"Bot :{reply_content}")
                
        msg_index = payload["messages"].index(message) 
        payload["messages"][msg_index]["content"] += reply_content
    
asyncio.run(main())