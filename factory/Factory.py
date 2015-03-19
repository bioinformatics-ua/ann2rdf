__author__ = 'Pedro Sernadela sernadela@ua.pt'

import logging

from factory import BioCFactory, AnnFactory, FactoryBase


class Factory:

    def __init__(self):
        self.annotations = list()

    def new_factory(self, filename):
        fact = None
        if str(filename).endswith('.xml'):
            fact = BioCFactory(filename)
        elif str(filename).endswith('.ann'):
            fact = AnnFactory(filename)
        else:
            raise ('No Factory found for %s', filename)

        if not isinstance(fact, FactoryBase):
            raise 'Class is not instance of FactoryBase'

        return fact
