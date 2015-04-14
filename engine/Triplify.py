__author__ = 'Pedro Sernadela sernadela@ua.pt'


import logging
from rdflib import URIRef, Literal, BNode
from rdflib.namespace import RDF, FOAF, XSD, DC, RDFS, Namespace
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

    def normalize(self, normalization):

        # For each ao:Annotation in the store get its ao:hasTopic property.
        '''
        topics = self.store.graph.objects(None, AO.hasTopic)
        for topic in topics:
            for value in self.store.graph.objects(topic, RDFS.label):
                norm_values = normalization.do_request(value)
                for norm_value in norm_values:

                    # try to convert 'GO:0005623' -> 'http://purl.org/obo/owl/GO#0005623'
                    if ':' in norm_value:
                        split = norm_value.split(':')
                        p = split[0].lower()
                        i = split[1].lower()
                        prefix = normalization.query_prefix_cc(p)
                        print prefix
                        if p in prefix:
                            self.store.bind(p, prefix[p])
                            self.store.add((topic, DC.related, URIRef(prefix[p]+i)))
                        else:
                            self.store.add((topic, DC.related, Literal(norm_value)))
                    else:

                    if str(norm_value).startswith('http'):
                        self.store.add((topic, DC.related, URIRef(norm_value)))
                    else:
                        self.store.add((topic, DC.related, Literal(norm_value)))
        '''

        annotations = self.store.graph.subjects(RDF.type, AO.Annotation)
        for annotation in annotations:
            contexts = self.store.graph.objects(annotation, AO.context)
            for context in contexts:
                for exact in self.store.graph.objects(context, AO.exact):
                    norm_values = normalization.normalize(exact)
                    for norm_value in norm_values:
                        if str(norm_value).startswith('http'):
                            self.store.add((annotation, AO.hasTopic, URIRef(norm_value)))
                        else:
                            self.store.add((annotation, AO.hasTopic, Literal(norm_value)))

    def process(self, annotations):

        # self.store.load('http://purl.org/ao/')

        # generate a unique id for the annotation set
        b_id = BNode()
        b_id = '_' + str(b_id)

        for annotation in annotations:

            # annotation
            ann_id = URIRef(self.namespace + annotation.id + b_id)
            self.store.add((ann_id, RDF.type, AO.Annotation))

            # context
            if annotation.context is not None:
                ann_context = URIRef(self.namespace + annotation.context.id + b_id)
                self.store.add((ann_context, RDF.type, AO.TextSelector))
                self.store.add((ann_context, AO.exact, Literal(annotation.context.exact)))
                for o in annotation.context.offset:
                    self.store.add((ann_context, AO.offset, Literal(o, datatype=XSD.integer)))
                for r in annotation.context.range:
                    self.store.add((ann_context, AO.range, Literal(r, datatype=XSD.integer)))
                self.store.add((ann_id, AO.context, ann_context))

            # tag
            for tag in annotation.tags:
                if str(tag).startswith('http'):
                    self.store.add((ann_id, AO.body, URIRef(tag)))
                else:
                    self.store.add((ann_id, AO.body, Literal(tag)))

            # relations
            for relation in annotation.relations:
                ann_target = URIRef(self.namespace + relation.annotation + b_id)
                # if relation is not specified generalize one
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
                self.store.add((ann_source, DC.identifier, Literal(annotation.source.id)))
                if annotation.source.retrievedFrom is not None:
                    self.store.add((ann_source, PAV.retrievedFrom, Literal(annotation.source.retrievedFrom)))
                if annotation.source.accessedOn is not None:
                    self.store.add((ann_source, PAV.sourceAccessedOn, Literal(annotation.source.accessedOn)))
                self.store.add((ann_id, AO.onSourceDocument, ann_source))

    # apply mappings available on the config file
    def map(self, mappings):
        tags = mappings['tags']
        relations = mappings['relations']

        for tag in tags:
            tag_to_remove = tag['if']
            tag_to_add = tag['then']
            for s in self.store.graph.subjects(AO.body, Literal(tag_to_remove)):
                self.store.remove((s, AO.body, Literal(tag_to_remove)))
                self.store.add((s, AO.body, Literal(tag_to_add)))

        for rel in relations:
            rel_to_remove = rel['if']
            rel_to_add = rel['then']
            rel_to_remove = URIRef(self.namespace + rel_to_remove)
            if str(rel_to_add).startswith('http'):
                rel_to_add = URIRef(rel_to_add)
            else:
                rel_to_add = URIRef(self.namespace + rel_to_add)
            for s, o in self.store.graph.subject_objects(rel_to_remove):
                self.store.remove((s, rel_to_remove, o))
                self.store.add((s, rel_to_add, o))

    def close(self):
        self.store.close()

    def show(self):
        s = self.store.serialize('turtle')
        logging.debug(s)

    def save_rdf(self, output):
        filename = output + '.rdf'
        s = self.store.serialize('xml')
        write_file(filename, s)
        logging.info('\nStore saved at: ' + filename)

    def save_ttl(self, output):
        filename = output + '.ttl'
        s = self.store.serialize('turtle')
        write_file(filename, s)
        logging.info('\nStore saved at: ' + filename)