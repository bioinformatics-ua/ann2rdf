__author__ = 'Pedro Sernadela sernadela@ua.pt'

import requests
import json
from jsonpath_rw import parse

PREFIX_CC = 'http://prefix.cc/'


class Normalization:

    def __init__(self, service, query):
        self.service = service
        self.query = query

    def do_request(self, text):
        try:
            headers = {'content-type': 'application/json'}
            payload = {'text': text}
            r = requests.post(self.service, data=json.dumps(payload), headers=headers)

            result = json.loads(r.text)

            path_expr = parse(self.query)

            values = []
            for match in path_expr.find(result):
                #print match.value
                if type(match.value) is list:
                    for m in match.value:
                        values.append(m)
                else:
                    values.append(match.value)

            values = set(values)

            # process ids
            for v in values:
                if ':' in v:
                    split = v.split(':')
                    values.remove(v)
                    values.add(split[0]+':'+split[1])
            #print values

            return values

        except requests.exceptions.RequestException:
            return []

    def query_prefix_cc(self, query):

        try:
            output = '.file.json'
            r = requests.get(PREFIX_CC+query+output)

            if r.status_code == 200:
                return json.loads(r.text)
            else:
                return {}

        except requests.exceptions.RequestException:
            return {}