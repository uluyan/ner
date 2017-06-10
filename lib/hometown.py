# -*- coding: utf-8 -*-
import jieba.posseg as pseg


def get_hometown(line):
    words = pseg.cut(line)
    word_one = ''
    word_two = ''
    for w in words:
        if not w.word.encode('utf-8').find('人') == -1:
            if not word_two == '':
                hometown = w.word[:-1].encode('utf-8')
                if not hometown == '':
                    prefixs = pseg.cut(hometown)
                    hometown = ''
                    for p in prefixs:
                        if not p.flag == 'ns':
                            continue
                        if not p.word.encode('utf-8').find('中国') == -1:
                            continue
                        if not p.word.encode('utf-8').find('中华') == -1:
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
