"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    Get random word from a file containing words

    >>> wf = WordFinder('words.txt')

    >>> wf.random()
        'nasoprognathic'

    >>> wf.random()
        'reunitedly'

    >>> wf.random()
        'marconi'
    """
    def __init__(self, file):
        self.file = file
        self.open_file = open(self.file, 'r')
        self.words = self.open_file.readlines()
        self.num_of_words = len(self.words)
        print(f'{self.num_of_words} words read')

        self.open_file.close()
        
    
    def random(self):
        """
        Get random index from list of words
        """
        random_ind = random.randint(0, self.num_of_words-1)
        return self.words[random_ind].strip()

        
    