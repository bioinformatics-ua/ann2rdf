__author__ = 'Pedro Sernadela sernadela@ua.pt'


import logging
from rdflib import URIRef, Literal, BNode
from rdflib.namespace import RDF, FOAF, Namespace
from Store import *


AO = Namespace('http://purl.org/ao/')

class Triplify:



    def __init__(self, prefix, namespace):
        self.prefix = prefix
        self.namespace = Namespace(namespace)
        self.store = Store()
        self.store.bind("ao", str(AO))

    def process(self, annotations):

        # self.store.load('http://purl.org/ao/')

        # logging.debug(self.store.serialize('turtle'))
        for annotation in annotations:
            guid = BNode()
            ann_id = URIRef(self.namespace + annotation.id + '_' + guid)
            #print ann
            self.store.add((ann_id, RDF.type, AO.annotation))

            #id = self.namespace.a
        self.store.show()
        self.store.close()

        # Create an identifier to use as the subject for Donna.
        # donna = BNode()
        # pedro = self.namespace.pedro

        # Add triples using store's add method.
        # self.store.add( (donna, RDF.type, FOAF.Person) )
        # self.graph.add( (pedro, RDF.type, FOAF.Person) )
        # self.graph.add( (donna, FOAF.nick, Literal("donna", lang="foo")) )
        # self.graph.add( (donna, FOAF.name, Literal("Donna Fales")) )
        # self.graph.add( (donna, FOAF.mbox, URIRef("mailto:donna@example.org")) )
        # self.graph.bind("foaf", FOAF)
        # self.graph.bind(self.prefix, self.namespace)
        #
        # s = self.store.serialize('turtle')
        # logging.debug(s)


