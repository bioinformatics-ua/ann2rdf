__author__ = 'Pedro Sernadela sernadela@ua.pt'


from Topic import *
from Annotation import *
from Context import *
from Relation import *
from Source import *
import logging


class AnnCreator:

    def __init__(self):
        self.id = ''
        self.annotations = list()

    def parse_bioc(self, bioc_file):

        annotations = list()

        # Go through each document
        for document in bioc_file.documents:

            source = Source(document.id.strip())
            source.accessedOn = bioc_file.date
            source.retrievedFrom = bioc_file.source

            # Go through each passage of the document
            for passage in document:
                # logging.debug(passage.text)

                source.text = passage.text

                # get annotations
                for annotation in passage.annotations:
                    ann = Annotation(annotation.id)
                    context = Context(annotation.id + '_' + annotation.text.strip())
                    context.exact = annotation.text.strip()

                    for key, infon in annotation.infons.iteritems():
                        topic = Topic(infon.strip())
                        topic.description = key
                        ann.add_topic(topic)
                        # logging.debug(annotation.id + " " + annotation.text.strip() + " " + key + " " + infon.strip())

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
                    r = ''
                    for key, infon in relation.infons.iteritems():
                        topic = Topic(infon.strip())
                        topic.description = key
                        ann.add_topic(topic)
                        r = relation.id + " " + key + " " + infon.strip()
                    for node in relation.nodes:
                        r = r + " " + node.refid
                        rel = Relation(node.role, node.refid)
                        ann.add_relation(rel)
                    ann.source = source
                    annotations.append(ann)
                    # logging.debug(r)

        return annotations
