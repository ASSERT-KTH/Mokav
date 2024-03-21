def func(*args):
	ret_values = []
	
	s = args[0]
	ret_values.append((s.swapcase() if (s[1:].isupper() or (len(s) == 1)) else s))

	return ret_values
