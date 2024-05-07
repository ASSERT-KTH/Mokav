def original_func(*args):
	global_list = []
	
	(k, b, n, t) = map(int, args[0].split())
	if (t == 1):
	    global_list.append(n)
	elif (k == 1):
	    global_list.append(max(0, (((((n * b) - t) + b) - 1) // b)))
	else:
	    (x, y, v) = (((k - 1) + b), ((t * (k - 1)) + b), 0)
	    while (x <= y):
	        x *= k
	        v += 1
	    global_list.append(max(0, ((n - v) + 1)))
	return global_list