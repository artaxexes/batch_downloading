# -*- coding: utf-8 -*-

import urllib.request

class ThisFile():
    def __init__(self, mime, filename, url):
        self.mime = mime
        self.filename = filename
        self.url = url + filename

    def check(self):
        opened = urllib.request.urlopen(self.url)
        return opened.info().__getitem__('Content-Type')

    def down(self, folder):
        path = folder + self.filename
        if self.check() == self.mime:
            urllib.request.urlretrieve(self.url, path)
