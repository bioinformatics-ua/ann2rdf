__author__ = 'Pedro Sernadela sernadela@ua.pt'


import logging
from rdflib import URIRef, Literal, BNode
from rdflib.namespace import RDF, FOAF, XSD, DC, Namespace
from Store import *
from file_utils import *

AO = Namespace('http://purl.org/ao/')
PAV = Namespace('http://purl.org/pav/')


class Triplify:

    def __init__(self, prefix, namespace):
        self.prefix = prefix
        self.namespace = Namespace(namespace)
        self.store = Store()
        self.store.bind(prefix, namespace)
        self.store.bind("ao", str(AO))
        self.store.bind("pav", str(PAV))
        self.store.bind("dc", str(DC))

    def process(self, annotations):

        # self.store.load('http://purl.org/ao/')

        # logging.debug(self.store.serialize('turtle'))
        for annotation in annotations:

            # annotation
            guid = BNode()
            ann_id = URIRef(self.namespace + annotation.id)
            self.store.add((ann_id, RDF.type, AO.annotation))

            # context
            if annotation.context is not None:
                ann_context = URIRef(self.namespace + annotation.context.id)
                self.store.add((ann_context, RDF.type, AO.TextSelector))
                self.store.add((ann_context, AO.exact, Literal(annotation.context.exact)))
                for o in annotation.context.offset:
                    self.store.add((ann_context, AO.offset, Literal(o, datatype=XSD.integer)))
                for r in annotation.context.range:
                    self.store.add((ann_context, AO.range, Literal(r, datatype=XSD.integer)))
                self.store.add((ann_id, AO.context, ann_context))

            # topic
            for topic in annotation.topics:
                ann_topic = URIRef(self.namespace + topic.id)
                self.store.add((ann_topic, DC.description, Literal(topic.description)))
                self.store.add((ann_id, AO.hasTopic, ann_topic))

            # relations
            for relation in annotation.relations:
                ann_target = URIRef(self.namespace + relation.annotation)
                if relation.relation:
                    ann_relation = URIRef(self.namespace + relation.relation)
                else:
                    ann_relation = DC.related
                self.store.add((ann_id, ann_relation, ann_target))

            # source
            if annotation.source is not None:
                ann_source = URIRef(self.namespace + annotation.source.id)
                self.store.add((ann_source, RDF.type, PAV.SourceDocument))
                self.store.add((ann_source, DC.description, Literal(annotation.source.text)))
                if annotation.source.retrievedFrom is not None:
                    self.store.add((ann_source, PAV.retrievedFrom, Literal(annotation.source.retrievedFrom)))
                if annotation.source.accessedOn is not None:
                    self.store.add((ann_source, PAV.sourceAccessedOn, Literal(annotation.source.accessedOn)))
                self.store.add((ann_id, AO.onSourceDocument, ann_source))

            #id = self.namespace.a
        # self.store.show()

        # Create an identifier to use as the subject for Donna.
        # donna = BNode()
        # pedro = self.namespace.pedro

        s = self.store.serialize('turtle')
        logging.debug(s)
        s = self.store.serialize('xml')
        write_file('test_files/slito.rdf', s)
        self.store.close()

