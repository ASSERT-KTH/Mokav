def func(*args):
	ret_values = []
	
	a = args[0]
	a = a.split()
	M = int(a[0])
	N = int(a[1])
	b = (N * M)
	c = (b // 2)
	ret_values.append(c)

	return ret_values
