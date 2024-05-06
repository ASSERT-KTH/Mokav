def original_func(*args):
	global_list = []
	
	n = int(args[0])
	a = (2 ** n)
	if (n > 31):
	    a -= ((2 ** 22) * 100)
	global_list.append(a)
	return global_list