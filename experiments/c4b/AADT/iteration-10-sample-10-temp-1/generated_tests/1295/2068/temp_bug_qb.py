def original_func(*args):
	global_list = []
	
	(n, k, l, c, d, p, nl, np) = map(int, args[0].split())
	x = round((((k * l) - ((k * l) % nl)) / nl))
	y = (c * d)
	z = round((p / np))
	if (x > y):
	    if (y > z):
	        global_list.append(int((z / n)))
	    else:
	        global_list.append(int((y / n)))
	elif (x > z):
	    global_list.append(int((z / n)))
	else:
	    global_list.append(int((x / n)))
	return global_list