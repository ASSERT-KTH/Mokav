def func(*args):
	ret_values = []
	
	(*l, a, b) = map(int, args[0].split())
	ret_values.append(max(0, (min((b + 1), *l) - a)))

	return ret_values
