def patched_func(*args):
	global_list = []
	
	(k, x) = map(int, args[0].split())
	y = 0
	while True:
	    if (((y % k) == 0) and y):
	        global_list.append((y // k))
	        break
	    if (((y + x) % k) == 0):
	        global_list.append(((y + x) // k))
	        break
	    y += 10
	return global_list