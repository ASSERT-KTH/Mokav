def original_func(*args):
	global_list = []
	
	(h1, h2) = map(int, args[0].split())
	(a, b) = map(int, args[1].split())
	(d, v) = (((h2 - h1) - (8 * a)), (12 * (a - b)))
	if (d <= 0):
	    global_list.append(0)
	elif (b >= a):
	    global_list.append((- 1))
	else:
	    global_list.append(((d + v) // v))
	return global_list