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
        genus = self.genus_builder.get_word()
        species = self.species_builder.get_word()
        return '%s %s' % (genus, species)


if __name__ == '__main__':
    namer = NominaFlora()
    for _ in range(5):
        print namer.get_name()
