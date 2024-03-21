def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split()))
	ret_values.append((max(a) - min(a)))

	return ret_values
