#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '

__author__ = 'renwotao'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__=='__main__':
	test()

'''
	作用域：
		__xxx__这样的特殊变量 比如__author__,__name__,__doc__
		_xxx 和__xxx 这样的含糊或变量是费公开的（private）不应该直接引用

'''

def _private_1(name):
	return 'Hello, %s' % name

def _private_2(name):
	return 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)


