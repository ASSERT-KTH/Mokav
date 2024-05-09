def patched_func(*args):
	global_list = []
	
	a = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = (int(args[0]) - 1)
	i = 5
	while (n >= i):
	    n -= i
	    i *= 2
	p = int((n / (i / 5)))
	global_list.append(a[p])
	return global_list