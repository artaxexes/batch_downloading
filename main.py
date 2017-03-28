#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import json
import downthefile

def mkdir():
    now = 'downloaded_{0:%Y}{0:%m}{0:%d}_{0:%H}{0:%M}{0:%S}'.format(datetime.datetime.now())
    try:
        print('Creating folder...')
        os.mkdir(now)
    except FileExistsError:
        pass
    except:
        print('Error: can not create folder')
        raise
    return now + '/'

def scan(filename):
    try:
        print('Reading ' + filename + '...')
        f = open(filename)
    except:
        print('Error: can not open ' + filename)
        pass
    else:
        handler = json.load(f)
        if handler['main_url'] == '' or handler['mime_type'] == '' or len(handler['files']) <= 0:
            print('Fill empty fields before start')
            raise
        path = mkdir()
        print('Downloading files...')
        for i in handler['files']:
             itm = downthefile.ThisFile(handler['mime_type'], i, handler['main_url'])
             itm.down(path)
        f.close()
    return

if __name__ == '__main__':
    print('Initializing...')
    scan('info.json')
    print('Done')
