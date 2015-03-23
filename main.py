__author__ = 'Pedro Sernadela sernadela@ua.pt'

import logging

from boot import *
from factory import Factory
from engine import Triplify, Normalization
import argparse
from os.path import isdir, isfile, join
from os import listdir


def main():
    # init logging
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        description="Annotations converter to RDF/XML.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', metavar="file_source", nargs=1,
                        default="config.json", help='Configuration file')
    parser.add_argument('--input', metavar="file", nargs=1,
                        default='test_files', type=str,
                        help='File or Folder to convert')
    parser.add_argument('--output', metavar="output_file", nargs=1,
                        default='test_files/output.rdf', type=str,
                        help='Output file')
    args = parser.parse_args()

    logging.debug(args)

    # return files from dir
    input_files = []
    if isdir(args.input):
        for f in listdir(args.input):
            input_files.append(args.input + '/' + f)
    else:
        input_files.append(args.input)

    # read configuration file
    b = Boot(args.config)
    #logging.debug(b.config_file)

    fact = Factory()
    for filename in input_files:
        logging.debug('\nStart loading: ' + filename)
        try:

            f = fact.new_factory(filename)
            file_content = f.parse()
            f.process(file_content)
            #for annotation in f.annotations:
                #logging.debug(annotation)
            logging.debug('Total annotations: ' + str(len(f.annotations)))

        except Exception as e:
            logging.error('Error loading: ' + filename)
            logging.error(e)

'''
            t = Triplify(b.prefix, b.namespace)
            t.process(f.annotations)
            n = Normalization(b.service, b.query)
            #t.normalize(n)
            #t.show()
            t.save(args.output)
            t.close()
'''
if __name__ == '__main__':
    main()