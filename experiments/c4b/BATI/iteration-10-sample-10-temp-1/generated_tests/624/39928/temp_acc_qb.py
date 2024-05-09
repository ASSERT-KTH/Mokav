def patched_func(*args):
	global_list = []
	
	(start, increment, check) = [int(x) for x in args[0].split(' ')]
	f = (((check - start) // increment) - 1)
	l = (((check - start) // increment) + 1)
	out = []
	for i in range(f, l):
	    out.append((start + (i * increment)))
	other = [(x + 1) for x in out if (x != start)]
	if (check < start):
	    global_list.append('NO')
	elif ((check in out) or (check in other)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list