from os.path import isfile


class Analyzer:# не читать файлы через read, рабоотать с ним как с последовательностью
    def __init__(self, filename):
        if isfile(filename):
            self.__filename = filename
        else:
            raise TypeError("wrong arguments")

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


try:
    a = Analyzer("docs/text.txt")
    print(a.countCharacters(), "Characters")
    print(a.countWords(), "Words")
    print(a.countSentences(), "Sentences")
except TypeError as e:
    print(e)

