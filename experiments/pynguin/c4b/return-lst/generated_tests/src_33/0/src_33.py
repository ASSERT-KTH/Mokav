def func(*args):
	ret_values = []
	
	n = int(args[0])
	e = int(args[1])
	for i in range(1, 31):
	    if ((n ** i) == e):
	        ret_values.append('YES')
	        ret_values.append((i - 1))
	        exit()
	ret_values.append('NO')

	return ret_values
