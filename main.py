__author__ = 'Pedro Sernadela sernadela@ua.pt'

# from bioc import BioCReader
# from bioc import BioCWriter
from boot import *
from abstraction import AnnCreator
import logging


def main():
    # init logging
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    # read configuration file
    b = Boot("config.json")
    logging.debug(b.config_file)

    t = AnnCreator()
    annotations = t.parse_bioc(b.bioc_file)
    for annotation in annotations:
        logging.debug(annotation)

if __name__ == '__main__':
    main()