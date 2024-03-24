def func(*args):
	ret_values = []
	
	s = str(args[0])
	if (s[1:].upper() == s[1:]):
	    ret_values.append(s.swapcase())
	else:
	    ret_values.append(s)

	return ret_values
