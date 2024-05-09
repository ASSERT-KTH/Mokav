def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	l1 = args[1]
	l = l1.split()
	x = len(l)
	for i in range(x):
	    l[i] = int(l[i])
	i = 0
	r = n
	sum = 0
	while (r > 0):
	    i = (i % 7)
	    r = (r - l[i])
	    if (r <= 0):
	        global_list.append(((i % 7) + 1))
	        i = 0
	        break
	    i += 1
	return global_list