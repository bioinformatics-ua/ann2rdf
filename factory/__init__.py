#
# Package for load different files format
#

__version__ = '1.0'

__author__ = 'Pedro Sernadela sernadela@ua.pt'


__all__ = ['Factory', 'FactoryBase', 'AnnFactory', 'BioCFactory']

from FactoryBase import FactoryBase
from AnnFactory import AnnFactory
from BioCFactory import BioCFactory
from Factory import Factory
