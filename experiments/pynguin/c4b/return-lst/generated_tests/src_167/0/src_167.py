def func(*args):
	ret_values = []
	
	'input\n92\n'
	n = int(args[0])
	l = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	if (n < 5):
	    ret_values.append(l[(n - 1)])
	else:
	    x = (- 1)
	    while (((10 * ((2 ** x) - 1)) + 6) <= n):
	        x += 1
	    x -= 1
	    x1 = int(((10 * ((2 ** x) - 1)) + 6))
	    ret_values.append(l[((n - x1) // (2 ** (x + 1)))])

	return ret_values
