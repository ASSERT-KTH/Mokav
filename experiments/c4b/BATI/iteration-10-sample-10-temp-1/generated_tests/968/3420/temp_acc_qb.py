def patched_func(*args):
	global_list = []
	
	(m, d) = map(int, args[0].split())
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if ((m == 2) and (d == 1)):
	    global_list.append(4)
	elif (d <= (5 + (31 - days[(m - 1)]))):
	    global_list.append(5)
	else:
	    global_list.append(6)
	return global_list