__author__ = 'Pedro Sernadela sernadela@ua.pt'

'''Class that identifies a Annotation.'''


class Annotation:
    def __init__(self, id):
        self.id = id
        self.tags = []
        self.relations = []
        self.context = None
        self.source = None

    def __str__(self):
        all_tags = ''
        for t in self.tags:
            all_tags += str(t)
        all_relations = ''
        for t in self.relations:
            all_relations += str(t)
        return '<Annotation>(' + self.id + ',' + str(self.context) + ',' + \
               str(self.source) + ',<Tag>[' + all_tags + '],[' + all_relations + '])'

    def add_tag(self, tag):
        self.tags.append(tag)

    def add_relation(self, relation):
        self.relations.append(relation)

    def __eq__(self, other):
        if isinstance(other, Annotation):
            return self.id == other.id
        return NotImplemented