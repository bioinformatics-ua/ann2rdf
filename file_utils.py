__author__ = 'Pedro Sernadela sernadela@ua.pt'

import json


def get_config_file(filename):
    try:
        f = open(filename)
        config_file = json.loads(f.read())
        f.close()
        return config_file
    except:
        return {}


def read_file(filename):
    try:
        f = open(filename)
        file_content = f.read()
        f.close()
        return file_content
    except:
        raise ('The file %s cannot be loaded.', filename)


def write_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    f.close()
