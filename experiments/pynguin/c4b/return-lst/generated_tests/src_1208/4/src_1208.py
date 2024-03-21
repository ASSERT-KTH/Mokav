def func(*args):
	ret_values = []
	
	import sys
	import math
	(a, b) = [int(x) for x in sys.stdin.readline().split()]
	n = 70
	k = ([True] * n)
	for i in range(2, int(math.sqrt(n))):
	    if k[i]:
	        for j in range((i ** 2), n, i):
	            k[j] = False
	if (not k[b]):
	    ret_values.append('NO')
	    exit()
	for i in range((a + 1), b):
	    if k[i]:
	        ret_values.append('NO')
	        exit()
	ret_values.append('YES')

	return ret_values
