def func(*args):
	ret_values = []
	
	(a, b) = args[0].split()
	a = int(a)
	b = int(''.join(reversed(b)))
	ret_values.append((a + b))

	return ret_values
