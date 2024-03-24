def func(*args):
	ret_values = []
	
	a = args[0]
	a = a.split()
	M = int(a[0])
	N = int(a[1])
	C = (M * N)
	if ((C % 2) == 0):
	    ret_values.append((C // 2))
	else:
	    ret_values.append((C // 2))

	return ret_values
