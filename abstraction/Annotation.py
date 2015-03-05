__author__ = 'Pedro Sernadela sernadela@ua.pt'


class Annotation:
    def __init__(self, id):
        self.id = id
        self.topic = []
        self.context = None
        self.source = None

    def __str__(self):
        return self.id + ' ' + str(self.topic) + ' ' + str(self.context)

    def add_topic(self, topic):
        self.topic.append(topic)