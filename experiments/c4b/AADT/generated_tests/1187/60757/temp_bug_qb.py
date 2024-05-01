def original_func(*args):
	global_list = []
	
	str = args[0]
	if str.isupper():
	    global_list.append(str.lower())
	elif str[0].islower():
	    if (len(str) == 1):
	        global_list.append(str.upper())
	    else:
	        global_list.append(str[0].upper(), str[1:].lower(), sep='')
	else:
	    global_list.append(str)
	return global_list