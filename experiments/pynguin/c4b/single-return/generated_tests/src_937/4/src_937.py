def func(*args):
	
	import math, re, sys, string, operator, functools, fractions, collections
	sys.setrecursionlimit((10 ** 7))
	RI = (lambda x=' ': list(map(int, args[0].split(x))))
	RS = (lambda x=' ': args[1].rstrip().split(x))
	dX = [(- 1), 1, 0, 0, (- 1), 1, (- 1), 1]
	dY = [0, 0, (- 1), 1, 1, (- 1), (- 1), 1]
	mod = int((1000000000.0 + 7))
	eps = 1e-06
	pi = math.acos((- 1.0))
	MAX = 100
	(a, b, r) = RI()
	return(['First', 'Second'][(min(a, b) < (2 * r))])
