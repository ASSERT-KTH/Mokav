def func(*args):
	ret_values = []
	
	s = args[0]
	if (len(s) == 1):
	    if s.islower():
	        ret_values.append(s.upper())
	    else:
	        ret_values.append(s.lower())
	elif (s[0].islower() and s[1:].isupper()):
	    ret_values.append((s[0].upper() + s[1:].lower()))
	elif s.isupper():
	    ret_values.append(s.lower())
	else:
	    ret_values.append(s)

	return ret_values
