def patched_func(*args):
	global_list = []
	
	
	def read():
	    return [int(x) for x in args[0].split()]
	(x, y) = read()
	i = 0
	while (x <= y):
	    x *= 3
	    y *= 2
	    i += 1
	global_list.append(i)
	return global_list