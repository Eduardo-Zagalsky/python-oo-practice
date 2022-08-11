"""Word Finder: finds random words from a dictionary."""
from random import choice
class WordFinder:
    """Reads a list of words and returns a random word

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read
    """
    def __init__(self, folder):
        self.folder = folder
        self.file = open(self.folder,"r")
        self.words = []
        for line in self.file:
            self.words.append(line)

    def random(self):
        random_word = choice(self.words)
        end = len(random_word)-1
        return random_word[:end]