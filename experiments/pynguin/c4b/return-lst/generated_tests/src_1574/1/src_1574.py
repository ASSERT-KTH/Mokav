def func(*args):
	ret_values = []
	
	[m, n] = args[0].split()
	m = int(m)
	n = int(n)
	ret_values.append(int(((m * n) / 2)))

	return ret_values
