def original_func(*args):
	global_list = []
	
	line = args[0].split()
	n = int(line[0])
	a = int(line[1])
	b = int(line[2])
	n -= a
	if (n > b):
	    n = ((n - b) + 1)
	global_list.append(n)
	return global_list