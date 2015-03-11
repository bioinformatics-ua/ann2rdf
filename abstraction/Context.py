__author__ = 'Pedro Sernadela sernadela@ua.pt'


class Context:
    def __init__(self, id):
        self.id = id
        self.offset = []
        self.range = []
        self.exact = ''

    def __str__(self):
        return '<Context>('+self.id + ',' + self.exact+')'

    def add_offset(self, offset):
        self.offset.append(offset)

    def add_range(self, range):
        self.range.append(range)
