def func(*args):
	ret_values = []
	
	(a, b) = args[0].split(' ')
	ret_values.append((int(a) + int(b[::(- 1)])))

	return ret_values
