# PyLlamaEdge

This is a Python library for LlamaEdge.

> [!NOTE]
> This library is in early development. The API is subject to change.

## Installation

To install the package, run the following command:

```bash
pip install llamaedge
```

## Usage

Here is an example of how to use the library to interact with the LlamaEdge server:

```python
from llamaedge.client import Client

# Create a LlamaEdge client with a specific server base URL
server_base_url = "http://localhost:8080"
client = Client(server_base_url)

messages = [
    {"role": "user", "content": "What is the capital of France?"},
]

# Send messages to the LlamaEdge server
response = client.chat(
    messages=messages
)

# Get the assistant's response
assistant_message = response["choices"][0]["message"]["content"]
print(assistant_message)
```

Note that the `server_base_url` should be the URL of the LlamaEdge server you want to connect to. To install the LlamaEdge server, refer to the section of [Deployment of LlamaEdge API Server](#deployment-of-llamaedge-api-server).

## Deployment of LlamaEdge API Server

Run the following command to deploy the LlamaEdge API server on macOS (Apple Silicon) or Linux (x86_64 with CUDA-12 support):

- macOS (Apple Silicon)

  ```bash
  cd ./deploy_llamaedge

  ./deploy_llamaedge_macos.sh

  # or, specify the ports
  ./deploy_llamaedge_macos.sh --proxy-port 10086 --llama-port 12345 --whisper-port 12306
  ```

- Linux

  ```bash
  cd ./deploy_llamaedge

  ./deploy_llamaedge_linux_x86_cuda12.sh

  # or, specify the ports
  ./deploy_llamaedge_linux_x86_cuda12.sh --proxy-port 10086 --llama-port 12345 --whisper-port 12306
  ```
