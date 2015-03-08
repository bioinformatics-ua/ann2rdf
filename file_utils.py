__author__ = 'Pedro Sernadela sernadela@ua.pt'

from bioc import BioCReader
import json


def get_config_file(filename):
    try:
        f = open(filename)
        config_file = json.loads(f.read())
        f.close()
        return config_file
    except:
        return {}


def parse_bioc_file(filename, dtd_file):
    bioc_reader = BioCReader(filename, dtd_valid_file=dtd_file)
    bioc_reader.read()
    return bioc_reader.collection

def parse_a1_file(filename):
    return true