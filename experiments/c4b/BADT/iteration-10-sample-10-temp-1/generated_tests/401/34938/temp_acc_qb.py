def patched_func(*args):
	global_list = []
	
	powers = [1, 2, 4]
	for i in range(3, 50):
	    if (i == 13):
	        powers.append(8092)
	    else:
	        powers.append((2 * powers[(i - 1)]))
	global_list.append(powers[int(args[0])])
	return global_list