__author__ = 'Pedro Sernadela sernadela@ua.pt'

import json
import logging
from os.path import isdir
from os import listdir


def get_config_file(filename):
    try:
        f = open(filename)
        config_file = json.loads(f.read())
        f.close()
        return config_file
    except IOError:
        logging.error('The configuration file cannot be loaded: ' + filename)
        return {}


def read_file(filename):
    try:
        f = open(filename)
        file_content = f.read()
        f.close()
        return file_content
    except IOError as e:
        logging.error('The file cannot be loaded: ' + filename)
        logging.error("I/O error({0}): {1}".format(e.errno, e.strerror))
    except Exception as e:
        logging.error(e)


def write_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    f.close()


# return files from dir
def get_files_from_dir(args_input):
    input_files = []
    if isdir(args_input):
        for f in listdir(args_input):
            input_files.append(args_input + '/' + f)
    else:
        input_files.append(args_input)
    return input_files


# extract filename id
def get_source_filename(filename):

    if '.' in filename:
        filename = filename.split('.')[0]

    if '/' in filename:
        filename = filename.split('/')[1]

    return filename
