def func(*args):
	ret_values = []
	
	import math, sys, re, itertools, pprint, collections, copy
	(ri, rai) = ((lambda : int(args[0])), (lambda : list(map(int, args[1].split()))))
	a = sys.stdin.readlines()
	ca = cb = 10
	for j in range(8):
	    for i in range(8):
	        if (a[i][j] == 'W'):
	            ca = min(ca, i)
	        if (a[i][j] == 'B'):
	            break
	for j in range(8):
	    for i in reversed(range(8)):
	        if (a[i][j] == 'B'):
	            cb = min(cb, (7 - i))
	        if (a[i][j] == 'W'):
	            break
	ret_values.append(('A' if (ca <= cb) else 'B'))

	return ret_values
