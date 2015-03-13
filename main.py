__author__ = 'Pedro Sernadela sernadela@ua.pt'


from boot import *
from abstraction import AnnCreator
from engine import Triplify, Normalization
import logging


def main():
    # init logging
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    # read configuration file
    b = Boot("config.json")
    logging.debug(b.config_file)

    ac = AnnCreator()
    annotations = ac.parse_bioc(b.bioc_file)
    for annotation in annotations:
        logging.debug(annotation)

    t = Triplify(b.prefix, b.namespace)
    t.process(annotations)

    n = Normalization(b.service, b.query)
    n.do_request()

if __name__ == '__main__':
    main()