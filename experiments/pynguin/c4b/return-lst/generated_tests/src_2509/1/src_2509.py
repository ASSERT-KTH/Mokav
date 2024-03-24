def func(*args):
	ret_values = []
	
	s = args[0]
	ret_values.append((s.count(max(s)) * max(s)))

	return ret_values
