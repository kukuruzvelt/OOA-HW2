class Analyzer:
    def __init__(self, filename):
        self.__filename = filename

    def countCharacters(self):
        with open(self.__filename) as f:
            text = f.read()
            text = text.split()
            text = ''.join(text)
        return len(text)

    def countWords(self):
        with open(self.__filename) as f:
            text = f.read()
            text = text.split()
        return len(text)

    def countSentences(self):
        with open(self.__filename) as f:
            text = f.read()
            text = text.count('.') + text.count('!') + text.count('?')
        return text


a = Analyzer("docs/text.txt")
print(a.countCharacters(), "Characters")
print(a.countWords(), "Words")
print(a.countSentences(), "Sentences")
