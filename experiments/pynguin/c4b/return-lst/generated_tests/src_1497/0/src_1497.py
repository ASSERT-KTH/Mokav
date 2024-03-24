def func(*args):
	ret_values = []
	
	s = args[0]
	k = len(s)
	if (k > 1):
	    if s.isupper():
	        ret_values.append(s.lower())
	    elif s[1:k].isupper():
	        ret_values.append((s[0].upper() + s[1:k].lower()))
	    else:
	        ret_values.append(s)
	else:
	    if s.isupper():
	        ret_values.append(s.lower())
	    if s.islower():
	        ret_values.append(s.upper())

	return ret_values
