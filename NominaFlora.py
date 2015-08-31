''' Produce latin names for flowers '''
from WordBuilder import WordBuilder

class NominaFlora(object):
    ''' Uses WordBuilder to create flower names '''

    def __init__(self):
        self.chunk_size = 2
        self.genus_builder = self.get_builder('genus')
        self.species_builder = self.get_builder('species')


    def get_builder(self, corpus):
        ''' creates a builder object for a wordlist '''
        builder = WordBuilder(chunk_size=self.chunk_size)
        builder.ingest(corpus)
        return builder


    def get_name(self):
        ''' Get a new flower name '''
        return self.genus_builder.get_word()


if __name__ == '__main__':
    namer = NominaFlora()
    print namer.get_name()
