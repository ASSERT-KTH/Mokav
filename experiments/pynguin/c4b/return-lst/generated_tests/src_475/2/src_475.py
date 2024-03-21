def func(*args):
	ret_values = []
	
	i = list(map(int, args[0].split()))
	ret_values.append((max(i) - min(i)))

	return ret_values
