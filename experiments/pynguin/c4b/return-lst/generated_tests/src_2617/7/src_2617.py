def func(*args):
	ret_values = []
	
	n = int(args[0])
	t = str(n)
	l = len(t)
	f = int(t[0])
	ret_values.append((((f + 1) * (10 ** (l - 1))) - n))

	return ret_values
