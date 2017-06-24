# -*- coding: utf-8 -*-

# split by key words
LIMIT = 10
KEYS = []
for year in range(1950, 2018):
    KEYS.append(str(year))


def cut(line):
    limit = 9999
    new_line = ''
    for i in range(len(line)):
        if limit < LIMIT:
            limit += 1
            new_line += line[i]
            continue
        key = line[i:i + 4]
        if key in KEYS:
            new_line += '\n'
            limit = 0
        new_line += line[i]
    return new_line

