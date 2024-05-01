def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = args[1]
	a = []
	a = s.split()
	for i in range(len(a)):
	    a[i] = int(a[i])
	i = 0
	while (n > 0):
	    n -= a[i]
	    i += 1
	    if (i > 6):
	        i = 0
	global_list.append(i)
	return global_list