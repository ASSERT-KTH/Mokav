def original_func(*args):
	global_list = []
	
	a = args[0].split()
	x = a.__len__()
	j = 0
	while (j < (x - 1)):
	    i = 0
	    while (i < (x - 1)):
	        if (a[i] < a[(i + 1)]):
	            (a[i], a[(i + 1)]) = (a[(i + 1)], a[i])
	        i += 1
	    j += 1
	global_list.append((abs((int(a[1]) - int(a[0]))) + abs((int(a[1]) - int(a[2])))))
	return global_list