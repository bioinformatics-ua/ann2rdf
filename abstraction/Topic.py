__author__ = 'Pedro Sernadela sernadela@ua.pt'


class Topic:
    def __init__(self, id):
        self.id = id
        self.description = None

    def __str__(self):
        return self.id + ' ' + self.description