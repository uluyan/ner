# -*- coding: utf-8 -*-
import os
import sys
from lib import cut

OUTPUT_DIR = 'data/out'


def cut_file(file_path, out_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    out = ''
    for line in lines:
        new_lines = cut(line)
        out += new_lines
    with open(out_path, 'w') as f:
        f.write(out)


def main(walk_dir):
    for root, dirs, files in os.walk(walk_dir):
        for f in files:
            file_path = os.path.join(root, f)
            out_path = os.path.join(OUTPUT_DIR, f)
            cut_file(file_path, out_path)


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.system('mkdir ' + OUTPUT_DIR)
    main(sys.argv[1])
