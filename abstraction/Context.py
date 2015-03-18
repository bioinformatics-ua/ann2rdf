__author__ = 'Pedro Sernadela sernadela@ua.pt'

'''Class that identifies the portion of the annotated resource(s).'''


class Context:
    def __init__(self, id):
        self.id = id
        '''identifies the exact string in a document through an offset'''
        self.offset = []
        '''number of characters - starting from the offset'''
        self.range = []
        '''The exact string - a linear sequence of characters - subject of the annotation.'''
        self.exact = ''

    def __str__(self):
        return '<Context>('+self.id + ',' + self.exact+')'

    def add_offset(self, offset):
        self.offset.append(offset)

    def add_range(self, range):
        self.range.append(range)
