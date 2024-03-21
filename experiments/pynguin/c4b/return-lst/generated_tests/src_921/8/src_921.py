def func(*args):
	ret_values = []
	
	s = args[0]
	a = {(s[i:] + s[:i]) for i in range(len(s))}
	ret_values.append(len(a))

	return ret_values
