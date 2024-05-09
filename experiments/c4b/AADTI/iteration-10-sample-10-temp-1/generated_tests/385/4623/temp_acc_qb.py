def patched_func(*args):
	global_list = []
	
	[h1, h2] = list(map(int, args[0].split()))
	[a, b] = list(map(int, args[1].split()))
	if ((h1 + (8 * a)) >= h2):
	    global_list.append(0)
	    exit(0)
	elif (a <= b):
	    global_list.append((- 1))
	    exit(0)
	d = (h1 + (8 * a))
	res = int(((((h2 - d) + (12 * (a - b))) - 1) / (12 * (a - b))))
	global_list.append(res)
	return global_list