# -*- coding: utf8 -*-
import re


def get_filename(fill_name):
    """读取文件名，去除文件夹路径和后缀"""
    return '.'.join(fill_name.split('/')[-1].split('.')[:-1])


def remove_punc(line):
    return re.sub('[：<>\-\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）\:]+'.decode('utf8'), ' ', line)
