def func(*args):
	ret_values = []
	
	string = args[0]
	if (string.isupper() or (string[0].islower() and string[1:].isupper())):
	    ret_values.append(''.join(((c.lower() if c.isupper() else c.upper()) for c in string)))
	elif ((len(string) == 1) and string.islower()):
	    ret_values.append(string.upper())
	else:
	    ret_values.append(string)

	return ret_values
