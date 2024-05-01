def patched_func(*args):
	global_list = []
	
	(n, a) = map(int, args[0].split())
	i = 1
	c = 0
	if ((a % 2) != 0):
	    while (i != a):
	        c = (c + 1)
	        i += 2
	    global_list.append((c + 1))
	i = n
	if ((a % 2) == 0):
	    while (i != a):
	        c += 1
	        i -= 2
	    global_list.append((c + 1))
	return global_list