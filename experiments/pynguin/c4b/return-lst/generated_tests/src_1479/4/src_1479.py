def func(*args):
	ret_values = []
	
	s = args[0]
	if (s[0].islower() and s[1:].isupper()):
	    ret_values.append(s.capitalize())
	elif s.isupper():
	    ret_values.append(s.lower())
	elif ((len(s) == 1) and s.islower()):
	    ret_values.append(s.upper())
	else:
	    ret_values.append(s)

	return ret_values
