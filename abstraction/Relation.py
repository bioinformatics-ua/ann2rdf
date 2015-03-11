__author__ = 'Pedro Sernadela sernadela@ua.pt'


class Relation:
    def __init__(self, relation, annotation):
        self.relation = relation
        self.annotation = annotation

    def __str__(self):
        return '<Relation>(' + self.relation + ',' + self.annotation + ')'