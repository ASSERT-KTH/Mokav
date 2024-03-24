def func(*args):
	ret_values = []
	
	import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time
	sys.setrecursionlimit((10 ** 7))
	inf = (10 ** 9)
	n = int(args[0])
	if (n < 100):
	    ret_values.append(n)
	    sys.exit()
	a = [[_, set(map(int, list(str(_))))] for _ in range(100)]
	c = 99
	for k in range(2, 11):
	    t = (10 ** (k - 1))
	    for aa in a:
	        if (aa[0] < t):
	            aa[1] = (aa[1] | set([0]))
	    at = a[:]
	    for i in range(1, 10):
	        t = (i * (10 ** k))
	        for (ai, ae) in at:
	            ac = (ai + t)
	            if (ac > n):
	                ret_values.append(c)
	                sys.exit()
	            if (len(ae) < 2):
	                ae = (ae | set([i]))
	            if ((i in ae) and (len(ae) < 3)):
	                c += 1
	                a.append([ac, ae])

	return ret_values
