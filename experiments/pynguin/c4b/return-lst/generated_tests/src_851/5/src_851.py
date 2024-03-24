def func(*args):
	ret_values = []
	
	s = args[0]
	if s[1:].isupper():
	    if s.isupper():
	        ret_values.append(s.lower())
	    else:
	        ret_values.append(s.title())
	elif ((len(s) == 1) and s.islower()):
	    ret_values.append(s.upper())
	elif ((len(s) == 1) and s.isupper()):
	    ret_values.append(s.lower())
	else:
	    ret_values.append(s)

	return ret_values
