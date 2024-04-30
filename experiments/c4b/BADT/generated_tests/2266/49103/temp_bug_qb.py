def original_func(*args):
	global_list = []
	
	n = int(args[0])
	get = []
	x = 1
	out = ''
	for i in range(1, n):
	    x = ((x + i) % n)
	    if (i == (n - 1)):
	        out += str(x)
	    else:
	        out += (str(x) + ' ')
	global_list.append(out)
	return global_list