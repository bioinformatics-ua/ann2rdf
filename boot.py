__author__ = 'Pedro Sernadela sernadela@ua.pt'

from file_utils import *


class Boot:
    def __init__(self, config_location):
        self.config_file = get_config_file(config_location)
        self.bioc_file = parse_bioc_file(self.config_file["input"], self.config_file["dtd"])




