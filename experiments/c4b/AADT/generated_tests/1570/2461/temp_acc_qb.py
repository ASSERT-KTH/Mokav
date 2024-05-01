def patched_func(*args):
	global_list = []
	
	(k, b, n, t) = map(int, args[0].split())
	if (k == 1):
	    global_list.append(max(0, ((((n * b) - t) + b) // b)))
	else:
	    (x, y, v) = (((k - 1) + b), ((t * (k - 1)) + b), 0)
	    while ((x * k) <= y):
	        x *= k
	        v += 1
	    global_list.append(max(0, (n - v)))
	return global_list