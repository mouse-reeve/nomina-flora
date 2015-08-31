''' Create words from an existing wordlist '''
import random
import re

class WordBuilder(object):
    ''' uses an existing corpus to create new phonemically consistent words '''

    def __init__(self, initial='>', terminal='<', chunk_size=2):
        #indicators for start and ends of words - set if necessary to avoid collision
        self.initial = initial
        self.terminal = terminal

        self.chunk_size = chunk_size

        self.links = {
            self.initial: []
        }


    def ingest(self, corpus_file):
        ''' load and parse a pre-formatted and cleaned text file. Garbage in, garbage out '''
        corpus = open(corpus_file)
        for word in corpus.readlines():
            # clean word
            word = word.strip()
            word = re.sub(r'[\',\.\"]', '', word)

            # iterate through n letter groups, where 1 <= n <= 3
            n = self.chunk_size
            start = 0
            # >: C, Cys: t, yst: i
            self.links[self.initial].append(word[0:n])
            for position in range(n, len(word)):
                start = position - n if position - n >= 0 else 0
                base = word[start:position]
                if not base in self.links:
                    self.links[base] = []

                self.links[base].append(word[position])
            if not word[n:len(word)] in self.links:
                self.links[word[n:len(word)]] = []
            self.links[word[n:len(word)]].append(self.terminal)


    def get_word(self, word=None):
        ''' creates a new word '''
        word = word if not word == None else self.initial
        if not self.terminal in word:
            word += random.choice(self.links[word[-self.chunk_size:]])
            return self.get_word(word)
        return word
