import cohere


class Cohere:
    
    def __init__(self, api_key: str):
       self._co = cohere.Client(api_key)

    def generate(self, prompt: str) -> str:
        print(f"Generating: {prompt}")
        res = self._co.generate(prompt=prompt, model="command")
        print("Finished generation")
        return res.generations[0].text

    