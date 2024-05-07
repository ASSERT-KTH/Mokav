def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = ['', 'Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	k = 1
	s = 1
	while ((5 * s) < n):
	    k *= 2
	    s += k
	s -= k
	n = ((n - (5 * s)) // k)
	global_list.append(a[(n + 1)])
	return global_list