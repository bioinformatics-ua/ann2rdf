__author__ = 'Pedro Sernadela sernadela@ua.pt'

import logging

from boot import *
from factory import Factory


def main():
    # init logging
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    # read configuration file
    b = Boot("config.json")
    logging.debug(b.config_file)

    fact = Factory()

    for filename in b.files:
        f = fact.new_factory(filename)
        file_content = f.parse()
        annotations = f.process(file_content)
        for annotation in annotations:
            logging.debug(annotation)

'''
    ac = AnnCreator()
    annotations = ac.parse_bioc(b.bioc_file)
    for annotation in annotations:
        logging.debug(annotation)

    t = Triplify(b.prefix, b.namespace)
    t.process(annotations)
    n = Normalization(b.service, b.query)
    t.normalize(n)
    t.close()
'''
if __name__ == '__main__':
    main()