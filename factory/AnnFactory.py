__author__ = 'Pedro Sernadela sernadela@ua.pt'

from abstraction import *
from factory import FactoryBase
import logging
from file_utils import *


class AnnFactory(FactoryBase):

    def __init__(self, filename):
        super(AnnFactory, self).__init__(filename)

    def parse(self):
        file_content = read_file(self.filename)
        lines = file_content.split('\n')
        return lines

    def process(self, file_content):
        annotations = list()
        for line in file_content:

            # text-bound annotation (entity / event trigger)
            if str(line).startswith('T'):
                #print line
                values = self.get_text_annotations(line)

                ann = Annotation(values['id'])
                ann.add_tag(values['tag'])
                context = Context('context_' + values['id'])
                context.exact = values['text']
                context.add_offset(values['offset'])
                context.add_range(values['range'])
                ann.context = context
                annotations.append(ann)
            # event
            elif str(line).startswith('E'):
                print 'event'
            # event modification
            elif str(line).startswith('M'):
                print 'event modification'
            # relation
            elif str(line).startswith('R'):
                print 'relation'
            # normalization (external reference)
            elif str(line).startswith('N'):
                print 'normalization'
            else:
                pass
        return annotations

    def get_text_annotations(self, line):
        ann = {}

        tab = line.split('\t')
        ann['id'] = tab[0]
        ann['text'] = tab[2]
        space = tab[1].split(' ')
        ann['tag'] = space[0]
        ann['offset'] = space[1]
        ann['range'] = space[2]

        return ann

