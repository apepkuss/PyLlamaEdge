import os
from typing import Optional

import requests


class Client:
    def __init__(self, server_base_url: str = "http://localhost:8080"):
        self.server_base_url = server_base_url

    def chat(self, messages: list[dict]) -> dict:
        """
        Send a chat message to the server
        """
        chat_url = self.server_base_url + "/v1/chat/completions"
        headers = {"Content-Type": "application/json"}

        # 构造请求的 JSON 数据
        data = {
            "messages": messages,
            "model": "llama",
            "stream": False,
        }

        # 发送 POST 请求
        chat_completion_response = requests.post(chat_url, headers=headers, json=data)

        try:
            json_response = chat_completion_response.json()
        except requests.exceptions.JSONDecodeError:
            raise ValueError(
                f"Server returned invalid JSON response: {chat_completion_response.text[:100]}"
            )

        return json_response
