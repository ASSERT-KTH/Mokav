def func(*args):
	ret_values = []
	
	b = []
	a = str(args[0]).split()
	for i in range(4):
	    if (a[i] not in b):
	        b.append(a[i])
	ret_values.append((4 - len(b)))

	return ret_values
