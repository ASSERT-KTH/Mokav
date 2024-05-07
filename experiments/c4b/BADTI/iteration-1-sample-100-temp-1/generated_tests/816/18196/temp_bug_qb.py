def original_func(*args):
	global_list = []
	
	(a, b, c) = args[0].strip().split(' ')
	(a, b, c) = (int(a), int(b), int(c))
	m = max(a, b, c)
	if ((a == b) and (b == c)):
	    global_list.append(0)
	    exit()
	if ((a == m) and (b < a) and (c < a)):
	    global_list.append(((((2 * a) - 2) - b) - c))
	elif ((b == m) and (b > c)):
	    if (a < b):
	        global_list.append((((((b - 1) + b) - 1) - a) - c))
	    elif (a == b):
	        global_list.append((((2 * b) - a) - c))
	elif (m == c):
	    if ((a < c) and (b < c)):
	        global_list.append(((((c + c) - 2) - a) - b))
	    elif ((a == c) and (b < c)):
	        global_list.append(((c - 1) - b))
	    elif ((a < c) and (b == c)):
	        global_list.append(((c - 1) - a))
	return global_list