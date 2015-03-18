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


def write_file(filename, content):
    f = open(filename, 'w')
    f.write(content)
    f.close()
