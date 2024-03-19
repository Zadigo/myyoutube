class TextAlgorithm:
    def __call__(self, text):
        return self.analyze(text)

    def analyze(self, text):
        return text


text_algorithm = TextAlgorithm()
