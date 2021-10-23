from os.path import isfile
import re


class Analyzer:
    """ Class for working with text file. """

    def __init__(self, filename):
        """ Initializes variables. """
        if isfile(filename):
            self.__filename = filename
        else:
            raise ValueError("wrong value")

    def countCharacters(self):
        """ Counts and returns the number of characters. """
        with open(self.__filename) as f:
            text = f.read()
            text = text.split()
            text = ''.join(text)
        return len(text)

    def countWords(self):
        """ Counts and returns the number of words. """
        with open(self.__filename) as f:
            text = f.read()
            text = re.sub(r'[^\'^\w]', ' ', text)
            text = text.split()
        return len(text)

    def countSentences(self):
        """ Counts and returns the number of sentences. """
        with open(self.__filename) as f:
            text = f.read()
            text = re.sub(' ', '', text)
            text = re.split('[.!?][a-z]', text)
        return len(text)


try:
    analyzer = Analyzer("docs/text.txt")
    print(analyzer.countCharacters(), "Characters")
    print(analyzer.countWords(), "Words")
    print(analyzer.countSentences(), "Sentences")
except ValueError as e:
    print(e)
