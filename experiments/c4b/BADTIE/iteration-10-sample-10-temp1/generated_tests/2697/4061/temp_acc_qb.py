def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	(r, l) = map(int, args[1].split())
	for i in range(0, 101):
	    for j in range(101):
	        if (((a * i) + b) == (l + (r * j))):
	            global_list.append(((a * i) + b))
	            exit()
	global_list.append((- 1))
	return global_list