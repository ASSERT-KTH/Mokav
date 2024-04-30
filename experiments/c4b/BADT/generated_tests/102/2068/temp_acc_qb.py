def patched_func(*args):
	global_list = []
	
	d = [int(i) for i in args[0].split()]
	i = 0
	while (i < 2):
	    if (d[i] > d[(i + 1)]):
	        (d[i], d[(i + 1)]) = (d[(i + 1)], d[i])
	        i = (- 1)
	    i += 1
	if (((2 * d[0]) + (2 * d[1])) < ((d[0] + d[1]) + d[2])):
	    global_list.append(((2 * d[0]) + (2 * d[1])))
	else:
	    global_list.append(((d[0] + d[1]) + d[2]))
	return global_list