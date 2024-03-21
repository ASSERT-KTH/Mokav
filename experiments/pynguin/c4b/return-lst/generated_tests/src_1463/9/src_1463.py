def func(*args):
	ret_values = []
	
	string = args[0]
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	firstletter = string[0]
	if ((firstletter in alpha) and (string[1:] == string[1:].upper())):
	    string = string.capitalize()
	    ret_values.append(string)
	elif (string == string.upper()):
	    ret_values.append(string.lower())
	else:
	    ret_values.append(string)

	return ret_values
