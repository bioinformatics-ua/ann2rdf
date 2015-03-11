__author__ = 'Pedro Sernadela sernadela@ua.pt'


class Source:
    def __init__(self, id):
        self.id = id
        self.retrievedFrom = None
        self.accessedOn = None
        self.text = ''

    def __str__(self):
        return '<Source>(' + self.id + ',' + str(self.retrievedFrom) + ',' + str(self.accessedOn) + ')'