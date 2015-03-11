__author__ = 'Pedro Sernadela sernadela@ua.pt'

from rdflib import Graph
import logging


class Store:

    def __init__(self):
        self.graph = Graph()

    def add(self, (s, p, o)):
        self.graph.add((s, p, o))

    def load(self, url):
        self.graph.load(url)

    def bind(self, prefix, namespace):
        self.graph.bind(prefix, namespace)

    def show(self):
        logging.debug("graph has %s statements." % len(self.graph))
        for s, p, o in self.graph:
            logging.debug(s+' '+p+' '+o)

    def serialize(self, format_type):
        return self.graph.serialize(format=format_type)

    def close(self):
        self.graph.close()