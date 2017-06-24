# -*- coding: utf-8 -*-
import os
import sys
from map import list2map

def show(db, num):
    word_list = []
    for node in db:
        if node[num] == '':
            continue
        word_list.append(node[num])
    map_list = []
    out_list = list2map(word_list, map_list)
    out = ''
    top = 15
    for o in out_list:
        if top == 0:
            break
        top -= 1
        out += '{0}:{1}\n'.format(o['key'], o['value'])
    print out[:-1]



def load(csv_path):
    """load csv data"""
    db = []
    with open(csv_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        cols = line.split(',')
        db.append(cols)
    show(db, int(sys.argv[1]))


if __name__ == '__main__':
    load('out.csv')

