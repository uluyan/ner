# -*- coding: utf-8 -*-
import jieba.posseg as pseg


def get_education(line):
    words = pseg.cut(line)
    for w in words:
        print w.word, w.flag


if __name__ == '__main__':
    line = '1975-1978年 东北林业大学道桥系学习'
    print get_education(line)
