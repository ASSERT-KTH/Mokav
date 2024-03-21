def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split()))
	ret_values.append((4 - len(set(a))))

	return ret_values
