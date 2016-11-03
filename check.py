#!/usr/bin/python

import os

files = os.listdir('img/')
print len(files), 'files'

lines = []
with open('info.txt') as f:
  for line in f:
    lines.append(line)
f.close()
print len(lines), 'lines'

print '\nlines not in files:'
for line in lines:
  img = line.partition('\n')
  if img[0] not in files:
    print img[0]
