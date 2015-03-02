__author__ = 'Pedro Sernadela sernadela@ua.pt'

# from bioc import BioCReader
# from bioc import BioCWriter
from boot import *
import logging


def main():
    # init logging
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    # read configuration file
    b = Boot("config.json")
    logging.debug(b.config_file)

    # Go through each document
    for document in b.bioc_file.documents:

        # Go through each passage of the document
        for passage in document:
            # logging.debug(passage.text)

            # get annotations
            for annotation in passage.annotations:
                for key, infon in annotation.infons.iteritems():
                    logging.debug(annotation.id + " " + annotation.text.strip() + " " + key + " " + infon.strip())

            # get relations
            for relation in passage.relations:
                r = ""
                for key, infon in relation.infons.iteritems():
                    r = r + relation.id + " " + key + " " + infon.strip()
                for node in relation.nodes:
                    r = r + " " + node.refid
                logging.debug(r)

if __name__ == '__main__':
    main()