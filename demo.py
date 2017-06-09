# -*- coding: utf-8 -*-
"""
   基于规则的命名实体识别
"""
import os
import sys
from lib.Items import Items
import lib.utils as utils

OUTPUT_CSV = 'demo.csv'
DEGREE = {
    'b': [],
    'm': [],
    'd': [],
}


def set_education(edu, degree, items):
    if degree == 'b':
        items.BU = edu['university']
        items.BF = edu['university']
    elif degree == 'm':
        items.MU = edu['university']
        items.MF = edu['university']
    elif degree == 'd':
        items.DU = edu['university']
        items.DF = edu['university']


def work_on_end(items):
    """结束时，检查教育经历"""
    degree = ''
    if items.BU == '':
        degree = 'b'
    if items.MU == '':
        if not degree == '':
            return False
        degree = 'm'
    if items.DU == '':
        if not degree == '':
            return False
        degree = 'd'
    max_weight = 0
    match_edu = None
    for edu in DEGREE[degree]:
        if edu['weight'][degree] > max_weight:
            match_edu = edu
            max_weight = edu['weight'][degree]
    if match_edu is not None:
        set_education(edu, degree, items)


def get_edu(line, items):
    edu, new_line = utils.get_education(line)
    degree = utils.get_degree(edu['weight'])
    if degree == '':
        if edu['weight']['b'] > 0:
            DEGREE['B'].append(edu)
        if edu['weight']['m'] > 0:
            DEGREE['M'].append(edu)
        if edu['weight']['d'] > 0:
            DEGREE['D'].append(edu)
        return False
    set_education(edu, degree, items)
    get_edu(new_line, items)


def work_on_line(line, items):
    """
       读取一行文字，进行命名实体识别
    """
    get_edu(line, items)
    # [gender]
    if not line.find('男') == -1:
        items.gender = '男'
    elif not line.find('女') == -1:
        items.gender = '女'
    # [hometown]
    hometown = utils.get_hometown(line)
    if not hometown == '':
        items.hometown = hometown
    # [title]
    title = utils.get_title(line)
    if not title == '':
        items.title = title
    return True


def work_on_papar(paper_path):
    """
       读取一篇文章
    """
    items = Items()
    # [name]
    items.name = utils.get_filename(paper_path)
    with open(paper_path, 'r') as f:
        lines = f.readlines()
    total_count = 0
    sucess_count = 0
    for line in lines:
        if len(line.strip()) == 0:
            continue
        if work_on_line(line, items):
            sucess_count += 1
        total_count += 1
    items.save(OUTPUT_CSV)
    return sucess_count, total_count


def work_on_dir(dir_path):
    """
        读取目录下的所有文件
    """
    total_papar = 0
    total_line = 0
    sucess_line = 0
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.find('.txt') == -1:
                continue
            sc, tc = work_on_papar(os.path.join(root, f))
            total_line += tc
            sucess_line += sc
            total_papar += 1
    print 'total {0} paper; sucess line: {1}/{2}'.format(
        total_papar, sucess_line, total_line)


if __name__ == '__main__':
    if os.path.exists(OUTPUT_CSV):
        os.system('rm -rf ' + OUTPUT_CSV)
    work_on_dir(sys.argv[1])
