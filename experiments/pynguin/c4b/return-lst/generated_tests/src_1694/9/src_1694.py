def func(*args):
	ret_values = []
	
	d = {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
	ret_values.append(d[int(args[0])])

	return ret_values
