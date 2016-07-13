#!/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import sys

def add(a, b):
    return a + b;

def main():
    if len(sys.argv) < 3:
        print('usage: {} a b'.format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(add(a, b))

if __name__ == '__main__':
    main()
