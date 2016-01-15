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
landwriter = csv.DictWriter(outfile, landreader.fieldnames + ["GeoJSON", "WKT"])
landwriter.writeheader()

limit = 6000

for cells in landreader:
    query_url = 'http://twland.ronny.tw/index/search?lands[]=' + cells['縣市別'] + ',' + cells['段名'] + ',' + cells['地號']
    r = requests.get(query_url)
    if len(r.json()['features']) > 0:
        r.json()['features']
        cells['GeoJSON'] = json.dumps(r.json())
        try:
            i = 0
            while r.json()['features'][i]['geometry'] == None :
                i = i + 1
            # incomplete WKT
            cells['WKT'] = geomet.wkt.dumps({
                'type': 'Polygon',
                'coordinates': r.json()['features'][i]['geometry']['coordinates'][0]
            })
        except Exception:
            sys.stdout.write(query_url + "\n")
            sys.stdout.flush()
    landwriter.writerow(cells)
    limit = limit - 1
    time.sleep(10)
    sys.stderr.write('.')
    sys.stderr.flush()
    if limit < 0:
        break
