#!/bin/env python
from elasticsearch import Elasticsearch
import json

query2 = {
    "query": {
        "query_string": {
            "query": "WARNING"
        }
    }
}

host_es = '10.86.64.31'
index_name = 'test_data'

es = Elasticsearch([{'host': host_es, 'port': 9200}], send_get_body_as='POST')
a = es.search(index=index_name, body=query2, analyze_wildcard = True)
print json.dumps(a, indent=4)
