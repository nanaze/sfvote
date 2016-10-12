# Python 2/3 compatability
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import collections
import csv
import sys

Item = collections.namedtuple('Item', ['name', 'value', 'url'])

def _YieldItems(csvfile):
  csvreader = csv.reader(csvfile)
  for row in csvreader:
    yield Item(*row)

def main():
  with open('spur.csv') as csvfile:
    print list(_YieldItems(csvfile))
    

if __name__ == '__main__':
  main()
