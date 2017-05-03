#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

def last_dir(path):
  dirs = []
  for entry in os.scandir(path):
    if entry.name.startswith('downloaded_') and entry.is_dir():
      dirs.append(entry.name)
  return max(dirs)

def file_content(filename):
  try:
    f = open(filename)
  except:
    print('Could not open the file')
  else:
    handler = json.load(f)
    f.close()
  return sorted(handler['files'])

def compare(lines, files):
  not_downloaded = []
  for line in lines:
    if line not in files:
      not_downloaded.append(line)
  return str(len(not_downloaded))

if __name__ == '__main__':
  lines = file_content('info.json')
  files = os.listdir(last_dir(os.getcwd()))
  print(compare(lines, files) + ' not downloaded')
