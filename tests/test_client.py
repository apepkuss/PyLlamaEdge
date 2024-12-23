import unittest

from llamaedge.client import Client


class TestChat(unittest.TestCase):
    def test_chat(self):
        client = Client(server_base_url="http://localhost:8080")
        response = client.chat(
            messages=[{"role": "user", "content": "What is the capital of France?"}]
        )
        assistant_message = response["choices"][0]["message"]["content"]
        # print(assistant_message)
        self.assertTrue("Paris" in assistant_message)

    def test_whisper(self):
        client = Client(server_base_url="http://localhost:8080")
        wav_file = "./tests/assets/test.wav"
        text = client.transcribe(wav_file)
        # print(text)
        self.assertTrue("This is a test record for whisper.cpp" in text)


if __name__ == "__main__":
    unittest.main()
