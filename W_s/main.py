#!/usr/bin/python3
import json
from pprint import pprint

with open('./JSON/logs.json') as f:
    data = json.load(f)

pprint(data)
