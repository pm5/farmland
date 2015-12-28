#!/usr/bin/env python

import csv
import requests
import json
import geomet.wkt
import time
import sys

csvfile = open('data/sgw-epa.csv', 'r')
outfile = open('data/sgw-epa-geom.csv', 'w')
landreader = csv.DictReader(csvfile)
landwriter = csv.DictWriter(outfile, landreader.fieldnames)
landwriter.writeheader()

limit = 6000

for cells in landreader:
    query_url = 'http://twland.ronny.tw/index/search?lands[]=' + cells['縣市別'] + ',' + cells['場址地號'] + ',' + cells['號']
    r = requests.get(query_url)
    if len(r.json()['features']) > 0:
        cells['GeoJSON'] = json.dumps(r.json())
        try:
            cells['WKT'] = geomet.wkt.dumps({
                'type': 'Polygon',
                'coordinates': r.json()['features'][0]['geometry']['coordinates'][0]
            })
        except Exception:
            sys.stderr.write("\n")
            print(query_url)
    landwriter.writerow(cells)
    limit = limit - 1
    time.sleep(10)
    sys.stderr.write('.')
    if limit < 0:
        break
