def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = 'aabb'
	a = len(s)
	ret_values.append(((s * (n // a)) + s[:(n % a)]))

	return ret_values
