def func(*args):
	
	import sys
	import math
	n = int(sys.stdin.readline())
	a = []
	a.append(str(n))
	for i in range(1, n):
	    a.append(str(i))
	return(' '.join(a))
