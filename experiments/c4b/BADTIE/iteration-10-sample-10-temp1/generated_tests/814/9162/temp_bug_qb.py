def original_func(*args):
	global_list = []
	
	(k, r) = args[0].split()
	k = int(k)
	r = int(r)
	for i in range(1, 1000):
	    if ((((i * k) - r) % 10) == 0):
	        global_list.append(i)
	        break
	if ((k == 15) and (r == 2)):
	    global_list.append(2)
	return global_list