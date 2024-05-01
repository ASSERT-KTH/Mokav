def patched_func(*args):
	global_list = []
	
	import sys
	(n, a, b, c) = map(int, args[0].split())
	m = 0
	cnt = (4 - (n % 4))
	if ((n % 4) == 0):
	    m = 0
	elif (cnt == 1):
	    m = min(a, (b + c), ((c + c) + c))
	elif (cnt == 2):
	    m = min((a + a), b, (c + c))
	elif (cnt == 3):
	    m = min(((a + a) + a), (b + a), c)
	global_list.append(m)
	return global_list