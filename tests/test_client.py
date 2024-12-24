import unittest

from llamaedge.client import Client, Message

server_base_url = "http://localhost:8080"


class TestChat(unittest.TestCase):
    def test_message(self):
        message = Message(role="user", content="What is the capital of France?")
        self.assertEqual(message.role, "user")
        self.assertEqual(message.content, "What is the capital of France?")
        self.assertEqual(
            message.to_dict(),
            {"role": "user", "content": "What is the capital of France?"},
        )

    def test_messages(self):
        messages = [
            Message(role="user", content="What is the capital of France?"),
            Message(role="assistant", content="The capital of France is Paris."),
        ]
        dict_messages = [message.to_dict() for message in messages]
        self.assertEqual(
            dict_messages,
            [
                {"role": "user", "content": "What is the capital of France?"},
                {"role": "assistant", "content": "The capital of France is Paris."},
            ],
        )

    def test_chat(self):
        client = Client(server_base_url=server_base_url)
        response = client.chat(
            messages=[{"role": "user", "content": "What is the capital of France?"}]
        )
        assistant_message = response["choices"][0]["message"]["content"]
        # print(assistant_message)
        self.assertTrue("Paris" in assistant_message)

    def test_whisper(self):
        client = Client(server_base_url=server_base_url)
        wav_file = "./tests/assets/test.wav"
        text = client.transcribe(wav_file)
        # print(text)
        self.assertTrue("This is a test record for whisper.cpp" in text)


if __name__ == "__main__":
    unittest.main()
