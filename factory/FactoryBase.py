__author__ = 'Pedro Sernadela sernadela@ua.pt'


class FactoryBase(object):

    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        pass

    def process(self, file_content):
        pass
