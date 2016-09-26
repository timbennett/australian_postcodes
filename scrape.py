# scrape australian postcodes from auspost.com
# output file will have duplicate entries
# todo: remove duplicates, remove blank lines
#
# to fill out base url key parameter: 
#   1. go to http://auspost.com.au/postcode
#   2. inspect network activity
#   3. search for a postcode
#   4. extract key from request to auspost.com.au/api/postcode/search.txt

import requests
import csv

base_url = "http://auspost.com.au/api/postcode/search.txt?key=[32characterstringgoeshere]&q={}&limit=100"
filename = 'postcodes.csv'
for n in range(0,1000):
    r = requests.get(base_url.format("%03d" % (n)))
    with open(filename, 'a') as csv_filedescriptor:
        csv_writer = csv.writer(csv_filedescriptor)
        for x in r.content.split("\n"):
             csv_writer.writerow(x.split("|"))
