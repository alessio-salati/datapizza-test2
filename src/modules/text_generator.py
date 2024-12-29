class TextGenerator:
    def __init__(self):
        self.max_length = 100  # Valore di default

    def set_max_length(self, max_length: int):
        self.max_length = max_length
        
    def generate(self, prompt: str, max_length: int) -> str:
        # genera testo dato un prompt
        return f"Generated text based on: {prompt}"
