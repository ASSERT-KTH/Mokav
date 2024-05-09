def original_func(*args):
	global_list = []
	
	a = args[0]
	a = a.split()
	for i in range(3):
	    a[i] = int(a[i])
	if (a[2] > (a[0] + a[1])):
	    a[2] = (a[0] + a[1])
	global_list.append(((a[0] + a[1]) + a[2]))
	return global_list