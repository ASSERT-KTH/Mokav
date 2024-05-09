def patched_func(*args):
	global_list = []
	
	'input\n508\n'
	from math import gcd
	(n, m) = (int(args[0]), 0)
	if (n <= 3):
	    global_list.append([1, 2, 6][(n - 1)])
	elif ((n % 2) == 1):
	    global_list.append(((n * (n - 1)) * (n - 2)))
	elif ((n % 3) == 0):
	    global_list.append((((n - 1) * (n - 2)) * (n - 3)))
	else:
	    global_list.append(((n * (n - 1)) * (n - 3)))
	return global_list