def patched_func(*args):
	global_list = []
	
	(k, a, b) = map(int, args[0].split())
	first = ((a // k) * k)
	if (first < a):
	    first += k
	last = ((b // k) * k)
	if (last > b):
	    last -= k
	if (last < first):
	    global_list.append(0)
	elif (last == first):
	    global_list.append(1)
	else:
	    global_list.append((((last - first) // k) + 1))
	return global_list