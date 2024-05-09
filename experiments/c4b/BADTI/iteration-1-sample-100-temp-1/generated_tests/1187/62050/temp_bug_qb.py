def original_func(*args):
	global_list = []
	
	string = args[0]
	if (string.isupper() or (string[0].islower() and string[1:].isupper())):
	    global_list.append(''.join(((c.lower() if c.isupper() else c.upper()) for c in string)))
	else:
	    global_list.append(string)
	return global_list