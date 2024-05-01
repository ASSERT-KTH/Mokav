def original_func(*args):
	global_list = []
	
	string = args[0]
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	firstletter = string[0]
	if ((firstletter in alpha) and (string[1:] == string[1:].upper())):
	    string = string.capitalize()
	    global_list.append(string)
	elif (string == string.upper()):
	    global_list.append(string.lower())
	return global_list