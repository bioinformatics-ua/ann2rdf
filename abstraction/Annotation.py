__author__ = 'Pedro Sernadela sernadela@ua.pt'


class Annotation:
    def __init__(self, id):
        self.id = id
        self.topics = []
        self.relations = []
        self.context = None
        self.source = None

    def __str__(self):
        all_topics = ''
        for t in self.topics:
            all_topics += str(t)
        all_relations = ''
        for t in self.relations:
            all_relations += str(t)
        return '<Annotation>(' + self.id + ',' + str(self.context) + ',' + str(self.source) + ',[' + all_topics + '],[' + all_relations + '])'

    def add_topic(self, topic):
        self.topics.append(topic)

    def add_relation(self, relation):
        self.relations.append(relation)