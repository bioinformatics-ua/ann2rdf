__author__ = 'Pedro Sernadela sernadela@ua.pt'

import requests
import json


class Normalization:

    def __init__(self, service, query):
        self.service = service
        self.query = query

    def do_request(self):
        headers = {'content-type': 'application/json'}
        payload = {'text': 'mitochondrial'}
        r = requests.post(self.service, data=json.dumps(payload), headers=headers)
        print r.text