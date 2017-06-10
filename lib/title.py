# -*- coding: utf8 -*-
import jieba.posseg as pseg


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
