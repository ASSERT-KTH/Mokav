def func(*args):
	ret_values = []
	
	import string
	s = args[0]
	if (s == s.upper()):
	    ret_values.append(s.swapcase())
	elif ((s[0] == s[0].lower()) and (s[1:] == s[1:].upper())):
	    ret_values.append(s.capitalize())
	else:
	    ret_values.append(s)

	return ret_values
