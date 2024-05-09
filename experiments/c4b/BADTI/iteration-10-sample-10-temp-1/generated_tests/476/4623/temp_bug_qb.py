def original_func(*args):
	global_list = []
	
	n = int(args[0])
	res = (n / 3)
	res *= 2
	if ((n % 3) > 0):
	    res += 1
	global_list.append(res)
	return global_list