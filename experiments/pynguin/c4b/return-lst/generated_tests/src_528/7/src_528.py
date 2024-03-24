def func(*args):
	ret_values = []
	
	n = int(args[0])
	r = 1
	while ((r * 5) < n):
	    n -= (r * 5)
	    r *= 2
	names = ('Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard')
	ret_values.append(names[int(((n - 1) / r))])

	return ret_values
