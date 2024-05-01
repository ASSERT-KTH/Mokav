def patched_func(*args):
	global_list = []
	
	string = args[0]
	if ((len(string) == 1) and string[0].islower()):
	    global_list.append(string.swapcase())
	elif ((string[0].islower() and string[1:].isupper()) or string.isupper()):
	    global_list.append(string.swapcase())
	else:
	    global_list.append(string)
	return global_list