#!/usr/bin/env python3

import sys

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
        