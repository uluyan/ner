# -*- coding: utf-8 -*-
import sys


def view(col_num, csv_file, out_file):
    out = ''
    with open(csv_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line == '':
            continue
        items = line.split(',')
        view_col = items[col_num]
        out += '{0}\n'.format(view_col)
        # out += '{0},{1}\n'.format(items[0], view_col)
    with open(out_file, 'w') as f:
        f.write(out)


if __name__ == '__main__':
    col_num = 1
    csv_file = 'out.csv'
    out_file = 'view.csv'
    if len(sys.argv) > 1:
        col_num = int(sys.argv[1])
    view(col_num, csv_file, out_file)
