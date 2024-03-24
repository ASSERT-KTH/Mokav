def func(*args):
	ret_values = []
	
	x = list(map(int, args[0].split()))
	t = len(x)
	m = len(set(x))
	ret_values.append((t - m))

	return ret_values
