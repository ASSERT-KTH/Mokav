def patched_func(*args):
	global_list = []
	
	from math import ceil
	n = int(args[0])
	a = ['', 'Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	k = 1
	s = 1
	while ((5 * s) < n):
	    k *= 2
	    s += k
	s -= k
	n = (n - (5 * s))
	n = ceil((n / k))
	global_list.append(a[n])
	return global_list