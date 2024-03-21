def func(*args):
	ret_values = []
	
	s = args[0]
	if s.isupper():
	    ret_values.append(s.lower())
	elif ((s[0].lower() and s[1:].isupper()) if (len(s) > 1) else True):
	    ret_values.append((s[0].upper() + s[1:].lower()))
	else:
	    ret_values.append(s)

	return ret_values
