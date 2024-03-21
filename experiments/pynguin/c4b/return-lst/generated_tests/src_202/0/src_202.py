def func(*args):
	ret_values = []
	
	n = ''.join(sorted(args[0])[::(- 1)])
	ret_values.append((n[0] * n.count(n[0])))

	return ret_values
