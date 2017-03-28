# -*- coding: utf-8 -*-

import urllib.request

class ThisFile():
    def __init__(self, mime, filename, url):
        self.__mime = mime
        self.__filename = filename
        self.__url = url + filename

    def __check(self):
        opened = urllib.request.urlopen(self.__url)
        return opened.info().__getitem__('Content-Type')

    def down(self, folder):
        path = folder + self.__filename
        if self.__check() != self.__mime:
            print(self.__url + ' contains wrong mime type')
            return
        urllib.request.urlretrieve(self.__url, path)
