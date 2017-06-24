# -*- coding: utf-8 -*-
"""
   命名实体
"""


class Items(object):
    def __init__(self):
        self.name = ''
        self.org = ''
        self.gender = ''
        self.title = ''
        self.hometown = ''
        self.BU = ''
        self.BF = ''
        self.MU = ''
        self.MF = ''
        self.DU = ''
        self.DF = ''

    def __str__(self):
        return '{0.name},{0.org},{0.gender},{0.hometown},{0.title},{0.BU},{0.BF},{0.MU},{0.MF},{0.DU},{0.DF}'.format(self)

    def save(self, path):
        with open(path, 'a+') as f:
            f.write(str(self) + '\n')
