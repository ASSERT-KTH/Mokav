def patched_func(*args):
	global_list = []
	
	from math import *
	(n, m) = [int(j) for j in args[0].split()]
	if (n <= m):
	    global_list.append(n)
	else:
	    k = ceil((((- 1) + sqrt((1 + (8 * (n - m))))) / 2))
	    while ((k * (k + 1)) >= (2 * (n - m))):
	        k -= 1
	    k += 1
	    global_list.append((m + k))
	return global_list