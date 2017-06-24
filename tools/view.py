# -*- coding: utf-8 -*-
import os
import sys
ORIGIN_DIR = 'data/test/resumes'
REVIEW_DIR = 'data/review'


def view(col_num, csv_file, out_file):
    out = ''
    warn = ''
    with open(csv_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line == '':
            continue
        items = line.split(',')
        view_col = items[col_num]
        if view_col == '':
            old_path = os.path.join(ORIGIN_DIR, items[0] + '.txt')
            new_path = os.path.join(REVIEW_DIR, items[0] + '.txt')
            os.system('cp "' + old_path + '" "' + new_path + '"')
        out += items[0] + ',' + view_col + '\n'
    with open(out_file, 'w') as f:
        f.write(out)


if __name__ == '__main__':
    os.system('rm -rf ' + REVIEW_DIR + '/*')
    col_num = 1
    csv_file = 'out.csv'
    out_file = 'view.csv'
    if len(sys.argv) > 1:
        col_num = int(sys.argv[1])
    view(col_num, csv_file, out_file)

