def func(*args):
	ret_values = []
	
	(a, b) = map(str, args[0].split())
	ret_values.append((int(a) + int(b[::(- 1)])))

	return ret_values
