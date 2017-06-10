# -*- coding: utf-8 -*-
from lib.utils import get_education
from lib.utils import get_degree
from lib.utils import get_hometown

def test(line):
    edu, new_line = get_education(line)
    if edu is None:
        return False
    bmd = get_degree(edu['weight'])
    u = edu['university']
    f = edu['faculty']
    if bmd == 'b':
        print 'BU: ' + u + ', BF: ' + f
    elif bmd == 'm':
        print 'MU: ' + u + ', MF: ' + f
    elif bmd == 'd':
        print 'DU: ' + u + ', DF: ' + f
    else:
        print 'U: ' + u + 'F: ' + f
    test(new_line)

def test_hometown(line):
    print get_hometown(line)


if __name__ == '__main__': 
    line = ''
    test_hometown(line)
