# -*- coding: utf8 -*-
import jieba.posseg as pseg


def get_university(line):
    words = pseg.cut(line)
    # limit word
    limit_word = ''
    pre_list = []
    for w in words:
        word = w.word.encode('utf-8')
        if not word.find('大学') == -1:
            limit_word = word
            break
        elif not word.find('学校') == -1:
            limit_word = word
            break
        elif not word.find('党校') == -1:
            limit_word = word
            break
        elif not word.find('学校') == -1:
            limit_word = word
            break
        pre_list.append(w)
    if limit_word == '':
        return '', line
    # start word
    university = ''
    ifAppend = False
    for w in pre_list:
        word = w.word.encode('utf-8')
        if w.flag == 'ns':
            ifAppend = True
        if ifAppend:
            university += word
        if w.flag == 'x':
            ifAppend = False
            university = ''
    university += limit_word
    # new line
    new_line = ''
    for w in words:
        word = w.word.encode('utf-8')
        new_line += word
    return university, new_line


def get_faculty(line):
    words = pseg.cut(line)
    # limit word
    limit_word = ''
    pre_list = []
    for w in words:
        word = w.word.encode('utf-8')
        if not word.find('专业') == -1:
            limit_word = word
            break
        elif not word.find('系') == -1:
            limit_word = word
            break
        pre_list.append(w)
    if limit_word == '':
        return '', line
    # start word
    faculty = ''
    for w in pre_list:
        word = w.word.encode('utf-8')
        faculty += word
        if w.flag == 'x':
            faculty = ''
    faculty += limit_word
    # new line
    new_line = ''
    for w in words:
        word = w.word.encode('utf-8')
        new_line += word
    return faculty, new_line


def get_degree(p):
    degree = ['b', 'm', 'd']
    if p['b'] > p['m']:
        degree[0] = 'm'
        degree[1] = 'b'
    if p[degree[1]] > p['d']:
        degree[2] = degree[1]
        degree[1] = 'd'
    if p[degree[0]] > p[degree[1]]:
        temp = degree[1]
        degree[1] = degree[0]
        degree[0] = temp
    if p[degree[2]] > p[degree[1]]:
        return degree[2]
    else:
        return ''


def get_education(line):
    words = pseg.cut(line)
    isUf = False
    weight = {'b': 0, 'm': 0, 'd': 0}
    for w in words:
        word = w.word.encode('utf-8')
        if not word.find('本科') == -1:
            weight['b'] += 1
            isUf = True
        if not word.find('学士') == -1:
            weight['b'] += 1
            isUf = True
        if not word.find('硕士') == -1:
            weight['m'] += 1
            isUf = True
        if not word.find('博士') == -1:
            weight['d'] += 1
            isUf = True
        if not word.find('研究生') == -1:
            weight['m'] += 0.8
            isUf = True
        if not word.find('研究生') == -1:
            weight['d'] += 0.4
            isUf = True
        if not word.find('学位') == -1:
            isUf = True
        if not word.find('毕业') == -1:
            isUf = True
        if not word.find('学习') == -1:
            isUf = True
        if not word.find('专业') == -1:
            isUf = True
        if not word.find('学历') == -1:
            isUf = True
    if not isUf:
        return None, line
    university, new_line = get_university(line)
    if university == '':
        return None, new_line
    faculty, new_line = get_faculty(new_line)
    return {'university': university, 'faculty': faculty, 'weight': weight}, new_line
