__author__ = 'Pedro Sernadela sernadela@ua.pt'

import logging
from boot import *
from factory import Factory
from engine import Triplify, Normalization
import argparse
import traceback
from multiprocessing.pool import ThreadPool
import sys


fact = None
boot = None
counter = 0
annotations = []


def process(filename):

    global counter
    counter += 1
    sys.stdout.write('\rLOADING: '+str(counter) + ', ACTUAL FILE: ' + filename)
    sys.stdout.flush()

    global fact
    global boot

    try:
        logging.debug('\nStart parsing: ' + filename)
        f = fact.new_factory(filename)
        file_content = f.parse()
        f.process(file_content)
        f.generate_hash()
        annotations.extend(f.annotations)
        for annotation in f.annotations:
            logging.debug(annotation)
        logging.debug('Total annotations parsed: ' + str(len(f.annotations)))

    except Exception as e:
        logging.error('Error loading: ' + filename + ' Cause: ' + str(e))
        logging.debug(traceback.format_exc())


def main():

    parser = argparse.ArgumentParser(
        description="Annotations converter to RDF/XML.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--config', metavar="file_source",
                        default="config.json", help='Configuration file')
    parser.add_argument('--input', metavar="source",
                        default='test_files', type=str,
                        help='File or Folder to convert')
    parser.add_argument('--output', metavar="output_file",
                        default='output', type=str,
                        help='Output file')
    parser.add_argument('--debug', action='store_true',
                        help='Enable debug')

    args = parser.parse_args()
    print args

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
    global boot
    boot = Boot(args.config)
    # logging.debug(b.config_file)

    # init factory to parse annotations files
    global fact
    fact = Factory()

    # threading support
    p = ThreadPool(processes=8)
    p.map(process, input_files)
    p.close()
    p.join()

    sys.stdout.write('\n')
    sys.stdout.flush()

    # init triples service
    triplify = Triplify(boot.prefix, boot.namespace, boot.ontologies)

    # init normalization service
    normalization = Normalization(boot.normalization)

    triplify.process(annotations)

    sys.stdout.write('\nTriples processed.')
    sys.stdout.flush()

    triplify.map(boot.mappings)

    sys.stdout.write('\nTriples mapped.\n')
    sys.stdout.flush()

    logging.debug('Start normalization.')
    triplify.normalize(normalization)
    logging.debug('Triples normalized.')

    # print RDF content
    # t.show()

    # write RDF file
    triplify.save_rdf(args.output)
    triplify.save_ttl(args.output)

    # close temporary store
    triplify.close()

if __name__ == '__main__':
    main()
