def patched_func(*args):
	global_list = []
	
	'input\n6 11 6\n'
	from math import gcd
	(a, b, c) = map(int, args[0].split())
	for x in range(((c // a) + 1)):
	    if (((c - (x * a)) % b) == 0):
	        global_list.append('Yes')
	        break
	else:
	    global_list.append('No')
	return global_list