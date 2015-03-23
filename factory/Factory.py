__author__ = 'Pedro Sernadela sernadela@ua.pt'

import logging

from factory import BioCFactory, AnnFactory, FactoryBase


class Factory:

    def new_factory(self, filename):

        fact = None

        if str(filename).endswith('.xml'):
            fact = BioCFactory(filename)
        elif str(filename).endswith('.ann'):
            fact = AnnFactory(filename)
        else:
            raise Exception('Not supported file type: ' + filename)

        if not isinstance(fact, FactoryBase):
            raise Exception('Class is not instance of FactoryBase')

        return fact
