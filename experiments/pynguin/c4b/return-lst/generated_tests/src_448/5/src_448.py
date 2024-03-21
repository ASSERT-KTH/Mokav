def func(*args):
	ret_values = []
	
	a = sorted(map(int, args[0].split()))
	ret_values.append((a[(- 1)] - a[0]))

	return ret_values
