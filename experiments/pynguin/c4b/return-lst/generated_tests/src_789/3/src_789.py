def func(*args):
	ret_values = []
	
	n = int(args[0])
	mid = ((1 + n) // 2)
	ret_values.append(((mid + n) % (n + 1)))

	return ret_values
