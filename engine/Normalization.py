__author__ = 'Pedro Sernadela sernadela@ua.pt'

import requests
import json
from jsonpath_rw import parse

PREFIX_CC = 'http://prefix.cc/'


class Normalization:

    def __init__(self, services):
        self.services = services

    def normalize(self, text):
        values = set()
        for s in self.services:
            s_service = s['service']
            s_query = s['query']
            s_enable = s['enable']

            if s_enable:
                values = values.union(self.do_request(text, s_service, s_query))

        return values


    def do_request(self, text, service, query):

        try:
            headers = {'content-type': 'application/json'}
            payload = {'text': text}
            r = requests.post(service, data=json.dumps(payload), headers=headers)

            result = json.loads(r.text)

            path_expr = parse(query)

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