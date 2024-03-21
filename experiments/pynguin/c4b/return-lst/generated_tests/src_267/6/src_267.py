def func(*args):
	ret_values = []
	
	n = int(args[0])
	names = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	cnt = 1
	while (n > (cnt * 5)):
	    n -= (cnt * 5)
	    cnt *= 2
	ret_values.append(names[((n - 1) // cnt)])

	return ret_values
