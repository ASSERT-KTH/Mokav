def func(*args):
	ret_values = []
	
	s = args[0]
	if ((not s[1:]) or s[1:].isupper()):
	    if s[0].islower():
	        ret_values.append((s[0].upper() + s[1:].lower()))
	    else:
	        ret_values.append((s[0].lower() + s[1:].lower()))
	else:
	    ret_values.append(s)

	return ret_values
