def func(*args):
	ret_values = []
	
	n = set(map(int, args[0].split()))
	ret_values.append((4 - len(n)))

	return ret_values
