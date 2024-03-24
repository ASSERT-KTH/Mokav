def func(*args):
	ret_values = []
	
	string = args[0]
	if ((len(string) == 1) and string[0].islower()):
	    ret_values.append(string.swapcase())
	elif ((string[0].islower() and string[1:].isupper()) or string.isupper()):
	    ret_values.append(string.swapcase())
	else:
	    ret_values.append(string)

	return ret_values
