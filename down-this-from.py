#!/usr/bin/python

import re
import urllib

filename = 'info.txt'
with open(filename) as file_handler:
  for line in file_handler:
    print(line)
