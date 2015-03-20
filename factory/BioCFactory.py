__author__ = 'Pedro Sernadela sernadela@ua.pt'

from bioc import BioCReader
from abstraction import *
from factory import FactoryBase

BioC_DTD = 'bioc/dtd/BioC.dtd'


class BioCFactory(FactoryBase):

    def __init__(self, filename):
        super(BioCFactory, self).__init__(filename)

    def parse(self):
        bioc_reader = BioCReader(self.filename, dtd_valid_file=BioC_DTD)
        bioc_reader.read()
        return bioc_reader.collection

    def process(self, file_content):

        annotations = list()

        # Go through each document
        for document in file_content.documents:

            source = Source(document.id.strip())
            source.accessedOn = file_content.date
            source.retrievedFrom = file_content.source

            # Go through each passage of the document
            for passage in document:
                # logging.debug(passage.text)

                source.text = passage.text

                # get annotations
                for annotation in passage.annotations:
                    ann = Annotation(annotation.id)
                    context = Context('context_' + annotation.id)
                    context.exact = annotation.text.strip()

                    for key, infon in annotation.infons.iteritems():
                        if key is not 'file':
                            tag = infon.strip()
                            # tag.description = key
                            ann.add_tag(tag)
                            # logging.debug(annotation.id)

                    for location in annotation.locations:
                        context.add_offset(location.offset)
                        context.add_range(location.length)
                        # logging.debug(location.offset + location.length)

                    ann.context = context
                    ann.source = source
                    annotations.append(ann)

                # get relations
                for relation in passage.relations:
                    ann = Annotation(relation.id)
                    # r = ''
                    for key, infon in relation.infons.iteritems():
                        tag = infon.strip()
                        # tag.description = key
                        ann.add_tag(tag)
                        # r = relation.id + " " + key + " " + infon.strip()
                    for node in relation.nodes:
                        # r = r + " " + node.refid
                        rel = Relation(node.role, node.refid)
                        ann.add_relation(rel)
                    ann.source = source
                    annotations.append(ann)
                    # logging.debug(r)

        return annotations