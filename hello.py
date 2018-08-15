#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module 使用模块的测试'

__author__='hd'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello python!')
    elif len(args)==2:
        print('hello,%s!' % args[1])
    else:
        print('Too many args!')

if __name__=='__main__':
    test()        