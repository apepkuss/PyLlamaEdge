import os
from typing import Optional

import requests


class Whisper:
    """Create a Whisper object"""

    def __init__(self, server_base_url: str = "http://localhost:8080"):
        """
        Initialize the Whisper object

        :param server_base_url: The base URL of the Whisper server
        """
        self.server_url = server_base_url + "/v1/audio/transcriptions"

    def transcribe(
        self,
        audio_file: str,
        language: str = "en",
        max_length: Optional[int] = None,
        split_on_word: Optional[bool] = None,
        max_context: Optional[int] = None,
    ) -> str:
        """
        Transcribe an audio file to text

        :param audio_file: The path to the audio file
        :param language: The language of the audio file
        :param max_length: The maximum length of the transcription
        :param split_on_word: Whether to split the transcription on words
        :param max_context: The maximum context length
        :return: The transcription of the audio file
        """
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"The file {audio_file} does not exist")

        if max_length is None:
            max_length = 0
        if split_on_word is None:
            split_on_word = False
        if max_context is None:
            max_context = -1

        data = {
            "language": language,
            "max_len": str(max_length),
            "split_on_word": str(split_on_word).lower(),
            "max_context": str(max_context),
        }

        with open(audio_file, "rb") as file:
            files = {"file": file}

            # Send POST request
            response = requests.post(self.server_url, files=files, data=data)

            # Check if the request was successful
            response.raise_for_status()

            try:
                json_response = response.json()
            except requests.exceptions.JSONDecodeError:
                # Print the actual response content for debugging
                print(f"Server response: {response.text}")
                raise ValueError(
                    f"Server returned invalid JSON response: {response.text[:100]}"
                )

            if "text" not in json_response:
                raise ValueError(
                    f"Server response missing 'text' field: {json_response}"
                )

            return json_response["text"]