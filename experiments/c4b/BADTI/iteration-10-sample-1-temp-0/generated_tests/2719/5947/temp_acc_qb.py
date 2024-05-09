def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	i = 0
	while (a <= b):
	    i += 1
	    a = (a * 3)
	    b = (b * 2)
	    if (a > b):
	        global_list.append(i)
	        break
	return global_list