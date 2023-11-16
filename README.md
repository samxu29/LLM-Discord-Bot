# LLM-Discord-Bot
A Simple Discord Bot powered by locally run LLM using [llama.cpp](https://github.com/ggerganov/llama.cpp) & [llama.cpp python binding](https://github.com/abetlen/llama-cpp-python)

![demo](https://github.com/samxu29/LLM-Discord-Bot/blob/main/img/demo.png)

## Dependency 

### First you will want to install llama.cpp `webserver` 

Following instruction from [llama-cpp-python](https://github.com/abetlen/llama-cpp-python#web-server)

OR 👇

`llama-cpp-python` offers a web server which aims to act as a drop-in replacement for the OpenAI API.
This allows you to use llama.cpp compatible models with any OpenAI compatible client (language libraries, services, etc).

To install the server package and get started:

```bash
pip install llama-cpp-python[server]
python3 -m llama_cpp.server --model models/7B/llama-model.gguf
```
Similar to Hardware Acceleration section above, you can also install with GPU (cuBLAS) support like this:

```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python[server]
python3 -m llama_cpp.server --model models/7B/llama-model.gguf --n_gpu_layers 35
```

Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to see the OpenAPI documentation.


### Some other dependency
- `aiohttp`
- `asyncio`
- `json`
- `discord`
- `dotenv`

## Future Work
- [ ] Plan to implement them as telegram bots instead.
