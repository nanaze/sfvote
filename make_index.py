#!/usr/bin/env python

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

def _WriteTable(items, out):
  out.write('<table>\n')

  out.write('<tr>\n')  
  for name, _, _ in items:
    out.write('<th>%s</th>\n' % name)
  out.write('</tr>\n')

  out.write('<tr>')  
  for _, val, url in items:
    out.write('<td>\n')

    out.write('<a href="%s">%s</a>\n' % (url, val))
    out.write('</td>\n')

  out.write('</tr>\n')  

  out.write('</table>')

def main():
  out = sys.stdout

  
  spur_items = list(_YieldItems(open('spur.csv')))
    
  out.write('<!doctype html>\n')
  out.write('<html>\n')
  out.write('<body>\n')
  out.write('<h1>SPUR</h1>')
  _WriteTable(spur_items, out)
  
  out.write('</body>\n')
  out.write('</html>\n')
    
if __name__ == '__main__':
  main()
