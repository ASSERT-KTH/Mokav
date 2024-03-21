def func(*args):
	ret_values = []
	
	ret_values.append((4 - len(set(map(int, args[0].split())))))

	return ret_values
