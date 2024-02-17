from openai import OpenAI as OAI


class OpenAI:
    
    def __init__(self, api_key: str):
        self._client = OAI(api_key=api_key)
        
    def tts(self, text: str, filename: str = "output.mp3") -> str:
        
        res = self._client.audio.speech.create(
            model="tts-1",
            voice="shimmer",
            input=text,
        )
        
        res.stream_to_file(filename)
        return filename