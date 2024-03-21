def func(*args):
	ret_values = []
	
	s = args[0]
	(a, b) = (s.split(' ')[0], s.split(' ')[1])
	ret_values.append((int(a) + int(b[::(- 1)])))

	return ret_values
