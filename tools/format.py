# -*- coding: utf-8 -*-
import os
import sys


def rename(walk_dir):
    for root, dirs, files in os.walk(walk_dir):
        for f in files:
            name = os.path.join(root, f)
            new_name = os.path.join(root, f[22:])
            os.system('mv ' + name + ' ' + new_name)


if __name__ == '__main__':
    rename(sys.argv[1])
