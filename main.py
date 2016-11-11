#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import datetime
import json
import downthefile

def mkdir():
    now = '{0:%Y}.{0:%m}.{0:%d}.{0:%H}h{0:%M}m{0:%S}s'.format(datetime.datetime.now())
    try:
        os.mkdir(now)
    except FileExistsError:
        pass
    except:
        print("unexpected error")
        raise
    return now + '/'

def scan(path, filename):
    try:
        f = open(filename)
    except:
        pass
    else:
        handler = json.load(f)
        for i in handler['files']:
             itm = downthefile.ThisFile(handler['mime_type'], i, handler['main_url'])
             itm.down(path)
        f.close()

if __name__ == "__main__":
    scan(mkdir(), 'info.json')
