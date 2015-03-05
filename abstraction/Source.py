__author__ = 'Pedro Sernadela sernadela@ua.pt'


class Source:
    def __init__(self, id):
        self.id = id
        self.retrievedFrom = None
        self.accessedOn = None

    def __str__(self):
        return self.id + ' ' + self.retrievedFrom + ' ' + self.accessedOn