def func(*args):
	ret_values = []
	
	from functools import reduce
	from operator import *
	from math import *
	from sys import *
	setrecursionlimit((10 ** 7))
	RI = (lambda : list(map(int, args[0].split())))
	RS = (lambda : args[1].rstrip().split())
	(a, b, n) = RI()
	for i in range(10):
	    if ((((a * 10) + i) % b) == 0):
	        ret_values.append((str(((a * 10) + i)) + ('0' * (n - 1))))
	        exit(0)
	ret_values.append((- 1))

	return ret_values
