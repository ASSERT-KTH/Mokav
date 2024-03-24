def func(*args):
	ret_values = []
	
	l = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0].strip())
	i = 1
	while ((i * 5) < n):
	    n -= (i * 5)
	    i *= 2
	ret_values.append(l[((n - 1) // i)])

	return ret_values
