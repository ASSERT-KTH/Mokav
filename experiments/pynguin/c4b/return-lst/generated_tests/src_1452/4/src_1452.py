def func(*args):
	ret_values = []
	
	s = args[0]
	r = s[1:]
	if (r.isupper() or s.isupper()):
	    ret_values.append(s.swapcase())
	elif (len(s) == 1):
	    ret_values.append(s.swapcase())
	else:
	    ret_values.append(s)

	return ret_values
