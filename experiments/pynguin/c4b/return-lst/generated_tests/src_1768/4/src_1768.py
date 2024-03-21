def func(*args):
	ret_values = []
	
	s = args[0]
	if (len(s) == 1):
	    s = s.swapcase()
	else:
	    if (s[0].islower() and s[1:].isupper()):
	        s = s.swapcase()
	    if s.isupper():
	        s = s.swapcase()
	ret_values.append(s)

	return ret_values
