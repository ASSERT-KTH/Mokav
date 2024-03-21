def func(*args):
	ret_values = []
	
	from functools import reduce
	from operator import *
	from math import *
	from sys import *
	from string import *
	from collections import *
	setrecursionlimit((10 ** 7))
	dX = [(- 1), 1, 0, 0, (- 1), 1, (- 1), 1]
	dY = [0, 0, (- 1), 1, 1, (- 1), (- 1), 1]
	RI = (lambda : list(map(int, args[0].split())))
	RS = (lambda : args[1].rstrip().split())
	s = args[2]
	for i in range((len(s) - 1), (- 1), (- 1)):
	    if s[i].isalpha():
	        ans = (s[i] in 'AEIOUYaeiouy')
	        break
	ret_values.append(['NO', 'YES'][ans])

	return ret_values
