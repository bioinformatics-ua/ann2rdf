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

    # TODO: catch exceptions
    def process(self, file_content):

        source = Source(get_source_filename(self.filename))

        for line in file_content:

            # text-bound annotation (entity / event trigger)
            if str(line).startswith('T'):
                values = self.parse_T(line)
                ann = Annotation(values['id'])
                ann.add_tag(values['tag'])
                context = Context('context_' + values['id'])
                context.exact = values['text']
                context.add_offset(values['offset'])
                context.add_range(values['range'])
                ann.context = context
                ann.source = source
                self.annotations.append(ann)

            # event
            elif str(line).startswith('E'):
                values = self.parse_E(line)
                ann = Annotation(values['id'])
                rel_trigger = Relation('trigger', values['trigger'])
                ann.add_relation(rel_trigger)
                for v in values['targets']:
                    rel = Relation(v['tag'], v['target'])
                    ann.add_relation(rel)
                ann.source = source
                self.annotations.append(ann)

            # event modification
            elif str(line).startswith('M'):
                pass
            # relation
            elif str(line).startswith('R'):
                values = self.parse_R(line)
                ann = Annotation(values['id'])
                ann.add_tag(values['relation'])
                for v in values['relations']:
                    relation = Relation(v['tag'], v['target'])
                    ann.add_relation(relation)
                ann.source = source
                self.annotations.append(ann)

            # normalization (external reference)
            elif str(line).startswith('N'):
                values = self.parse_N(line)
                ann_to_find = Annotation(values['id'])
                index = self.annotations.index(ann_to_find)
                ann = self.annotations.__getitem__(index)
                ann.add_topic(values['reference'])
                # ann.add_tag(values['tag'])
                ann.source = source
                self.annotations.append(ann)

            # entity equivalence annotations
            elif str(line).startswith('*'):
                pass
            else:
                pass

    # parse text annotations (T) from line
    def parse_T(self, line):
        ann = {}
        tab = line.split('\t')
        ann['id'] = tab[0]
        ann['text'] = tab[2]
        space = tab[1].split(' ')
        ann['tag'] = space[0]
        ann['offset'] = space[1]
        ann['range'] = str(int(space[2]) - int(ann['offset']))
        return ann

    # parse event annotations (E) from line
    def parse_E(self, line):
        ann = {}
        tab = line.split('\t')
        ann['id'] = tab[0]
        events = []
        space = tab[1].split(' ')
        trigger = space[0]
        ann['trigger'] = trigger.split(':')[1]
        for s in space:
            if s is not trigger:
                res = s.split(':')
                event = {'tag': res[0], 'target': res[1]}
                events.append(event)
        ann['targets'] = events
        return ann

    # parse relations (R) from line
    def parse_R(self, line):
        ann = {}
        tab = line.split('\t')
        ann['id'] = tab[0]
        all_rel = tab[1].split(' ')
        ann['relation'] = all_rel[0]
        relations = []
        arg1 = all_rel[1].split(':')
        arg1_dict = {'tag': arg1[0], 'target': arg1[1]}
        relations.append(arg1_dict)
        arg2 = all_rel[2].split(':')
        arg2_dict = {'tag': arg2[0], 'target': arg2[1]}
        relations.append(arg2_dict)
        ann['relations'] = relations
        return ann

    # parse normalizations (N) from line
    def parse_N(self, line):
        ann = {}
        tab = line.split('\t')
        ref = tab[1].split(' ')
        ann['id'] = ref[1]
        ann['reference'] = ref[2]
        ann['tag'] = tab[2]
        return ann