from os.path import isfile


class Analyzer:
    """ Class for working with text file. """

    def __init__(self, filename):
        """ Checks arguments against values and initializes class variables. """
        if isfile(filename):
            self.__filename = filename
        else:
            raise ValueError("wrong value")

    def countCharacters(self):
        """ Counts and returns the number of characters. """
        with open(self.__filename) as f:
            num = 0
            while True:
                c = f.read(1)
                if c == '':
                    break
                elif not c == ' ':
                    num += 1
        return num

    def countWords(self):
        """ Counts and returns the number of words. """
        with open(self.__filename) as f:
            num = 1
            while True:
                c = f.read(1)
                if c == '':
                    break
                elif c == ' ':
                    num += 1
        return num

    def countSentences(self):
        """ Counts and returns the number of sentences. """
        with open(self.__filename) as f:
            num = 0
            while True:
                c = f.read(1)
                if c == '':
                    break
                elif c == '.' or c == '!' or c == '?':
                    num += 1
        return num


try:
    a = Analyzer("docs/text.txt")
    print(a.countCharacters(), "Characters")
    print(a.countWords(), "Words")
    print(a.countSentences(), "Sentences")
except ValueError as e:
    print(e)
