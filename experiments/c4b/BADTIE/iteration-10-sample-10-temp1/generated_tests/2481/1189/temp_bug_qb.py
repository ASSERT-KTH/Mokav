def original_func(*args):
	global_list = []
	
	n = int(args[0])
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	cnt = 1
	while (n > (cnt * 5)):
	    n -= (cnt * 5)
	    cnt += 1
	global_list.append(names[((n - 1) // cnt)])
	return global_list