def patched_func(*args):
	global_list = []
	
	'input\n92\n'
	n = int(args[0])
	l = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	if (n < 5):
	    global_list.append(l[(n - 1)])
	else:
	    x = (- 1)
	    while (((10 * ((2 ** x) - 1)) + 6) <= n):
	        x += 1
	    x -= 1
	    x1 = int(((10 * ((2 ** x) - 1)) + 6))
	    global_list.append(l[((n - x1) // (2 ** (x + 1)))])
	return global_list