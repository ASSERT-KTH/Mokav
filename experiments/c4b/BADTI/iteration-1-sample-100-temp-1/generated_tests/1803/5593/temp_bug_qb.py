def original_func(*args):
	global_list = []
	
	from math import gcd
	n = int(args[0])
	if (n < 2):
	    global_list.append(n)
	elif (not (n % 6)):
	    global_list.append((((n - 1) * (n - 2)) * (n - 3)))
	elif (not (n % 2)):
	    global_list.append(((n * (n - 1)) * (n - 3)))
	else:
	    global_list.append(((n * (n - 1)) * (n - 2)))
	return global_list