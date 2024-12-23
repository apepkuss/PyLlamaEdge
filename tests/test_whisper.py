import unittest

from llamaedge.whisper import Whisper


class TestWhisper(unittest.TestCase):
    def test_whisper(self):
        whisper = Whisper("http://localhost:12345")
        wav_file = "./tests/assets/test.wav"
        text = whisper.transcribe(wav_file)
        # print(text)
        self.assertTrue("This is a test record for whisper.cpp" in text)


if __name__ == "__main__":
    unittest.main()
