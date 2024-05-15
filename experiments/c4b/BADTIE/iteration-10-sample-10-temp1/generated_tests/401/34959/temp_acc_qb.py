def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = (2 ** n)
	if (n >= 13):
	    a -= ((2 ** (n - 13)) * 100)
	global_list.append(a)
	return global_list