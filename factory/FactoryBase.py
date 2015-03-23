__author__ = 'Pedro Sernadela sernadela@ua.pt'

'''
Base class to build a file format connector
'''


class FactoryBase(object):

    def __init__(self, filename):
        self.filename = filename
        self.annotations = list()

    '''
    Parse the file to a readable format
    '''
    def parse(self):
        pass

    '''
    Process the file according to the abstraction object model
    '''
    def process(self, file_content):
        pass
