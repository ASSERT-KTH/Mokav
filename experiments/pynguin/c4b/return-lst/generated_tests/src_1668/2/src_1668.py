def func(*args):
	ret_values = []
	
	n = args[0]
	ret_values.append((((int(n[0]) + 1) * (10 ** (len(n) - 1))) - int(n)))

	return ret_values
