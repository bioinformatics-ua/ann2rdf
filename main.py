__author__ = 'Pedro Sernadela sernadela@ua.pt'

import logging

from boot import *
from factory import Factory
from engine import Triplify, Normalization
import argparse
import traceback


def main():

    parser = argparse.ArgumentParser(
        description="Annotations converter to RDF/XML.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', metavar="file_source", nargs=1,
                        default="config.json", help='Configuration file')
    parser.add_argument('--input', metavar="source", nargs=1,
                        default='test_files', type=str,
                        help='File or Folder to convert')
    parser.add_argument('--output', metavar="output_file", nargs=1,
                        default='output', type=str,
                        help='Output file')
    parser.add_argument('--debug', action='store_false',
                        help='Enable debug')

    args = parser.parse_args()

    if args.debug:
        log_type = logging.DEBUG
    else:
        log_type = logging.INFO

    # init logging
    logging.basicConfig(format='%(message)s', level=log_type)
    logging.debug(args)

    # return files from dir else return file
    input_files = get_files_from_dir(args.input)

    # load configuration file
    b = Boot(args.config)
    # logging.debug(b.config_file)

    # init factory to parse annotations files
    fact = Factory()

    # init triples service
    t = Triplify(b.prefix, b.namespace)

    # init normalization service
    n = Normalization(b.normalization)

    for filename in input_files:

        try:
            logging.info('\nStart parsing: ' + filename)
            f = fact.new_factory(filename)
            file_content = f.parse()
            f.process(file_content)
            for annotation in f.annotations:
                logging.debug(annotation)
            logging.info('Total annotations parsed: ' + str(len(f.annotations)))

            t.process(f.annotations)
            logging.info('Triples processed.')
            t.map(b.mappings)
            logging.info('Triples mapped.')

            logging.info('Start normalization.')
            t.normalize(n)
            logging.info('Triples normalized.')

        except Exception as e:
            logging.error('Error loading: ' + filename + ' Cause: ' + str(e))
            logging.debug(traceback.format_exc())

    # print RDF content
    # t.show()

    # write RDF file
    t.save_rdf(args.output)
    t.save_ttl(args.output)

    # close temporary store
    t.close()

if __name__ == '__main__':
    main()