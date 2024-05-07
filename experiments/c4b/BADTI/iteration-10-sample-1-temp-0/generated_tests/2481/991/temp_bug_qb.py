def original_func(*args):
	global_list = []
	
	from math import ceil
	a = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0])
	m = n
	i = 1
	while (m > 0):
	    m -= (5 * i)
	    i += 1
	global_list.append(a[(ceil(((m + (5 * (i - 1))) / (i - 1))) - 1)])
	return global_list