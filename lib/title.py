# -*- coding: utf8 -*-
import jieba.posseg as pseg

YEARS = []
for y in range(1950, 2018):
    YEARS.append(str(y))


def get_by_years(line, words):
    hasTitle = False
    isStart = False
    title = ''
    for y in YEARS:
        if not line.find(y) == -1:
            hasTitle = True
    if not hasTitle:
        return ''
    word_list = []
    for w in words:
        word_list.append(w)
        word = w.word.encode('utf-8')
        if w.flag == 'eng':
            return ''
    for w in word_list:
        word = w.word.encode('utf-8')
        if not isStart:
            if w.flag[0] == ('n'):
                isStart = True
                title += word
        else:
            if w.flag == 'x':
                return title
            else:
                title += word
    return title


def get_title(line):
    words = pseg.cut(line)
    title = ''
    if line.find('现任') == -1:
        return get_by_years(line, words)
    for w in words:
        word = w.word.encode('utf-8')
        if word.find('现任') == -1:
            continue
        else:
            break
    for w in words:
        word = w.word.encode('utf-8')
        if w.flag == 'x':
            return title
        else:
            title += word
    return title

