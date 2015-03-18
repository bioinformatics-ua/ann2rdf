__author__ = 'Pedro Sernadela sernadela@ua.pt'

from abstraction import *
from factory import FactoryBase
import logging


class AnnFactory(object):

    def __init__(self, filename):
        self.filename = filename

    def parse(self):
        annotations = list()
        return annotations

    def process(self, file_content):
        annotations = list()
        return annotations