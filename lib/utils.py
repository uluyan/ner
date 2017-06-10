# -*- coding: utf8 -*-
"""
    通用工具
"""
import re
import jieba.posseg as pseg


def get_filename(fill_name):
    """读取文件名，去除文件夹路径和后缀"""
    return '.'.join(fill_name.split('/')[-1].split('.')[:-1])


def remove_punc(line):
    return re.sub('[：<>\-\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）\:]+'.decode('utf8'), ' ', line)


def get_hometown(line):
    words = pseg.cut(line)
    word_one = ''
    word_two = ''
    for w in words:
        if not w.word.encode('utf-8').find('人') == -1:
            if not word_two == '':
                hometown = w.word[:-1].encode('utf-8')
                print 'pre: ' + hometown
                if not hometown == '':
                    prefixs = pseg.cut(hometown)
                    hometown = ''
                    for p in prefixs:
                        if not p.flag == 'ns':
                            continue
                        hometown += p.word.encode('utf-8')
                    if hometown == '':
                        continue
                if word_two.flag == 'ns':
                    hometown = word_two.word.encode('utf-8') + word_one.word.encode('utf-8') + hometown
                elif word_one.flag == 'ns':
                    hometown = word_one.word.encode('utf-8') + hometown
                if not hometown == '':
                    return hometown
                    break
        word_two = word_one
        word_one = w
    return ''


def get_title(line):
    words = pseg.cut(line)
    hasTitle = False
    isStart = False
    title = ''
    for w in words:
        if not hasTitle:
            if w.flag == 'm':
                hasTitle = True
        elif not isStart:
            if not w.flag.find('n') == -1:
                isStart = True
                title += w.word.encode('utf-8')
        else:
            if w.flag == 'x':
                title += ' '
            else:
                title += w.word.encode('utf-8')
    return title


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
