def patched_func(*args):
	global_list = []
	
	string = args[0]
	if (string.isupper() or (string[0].islower() and string[1:].isupper())):
	    global_list.append(''.join(((c.lower() if c.isupper() else c.upper()) for c in string)))
	elif ((len(string) == 1) and string.islower()):
	    global_list.append(string.upper())
	else:
	    global_list.append(string)
	return global_list