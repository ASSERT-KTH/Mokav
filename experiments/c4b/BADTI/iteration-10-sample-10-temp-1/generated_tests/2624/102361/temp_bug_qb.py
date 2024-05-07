def original_func(*args):
	global_list = []
	
	a = int(args[0])
	sstring = []
	if (a % 2):
	    sstring.append('7')
	else:
	    a = a
	if (a % 2):
	    a = (a - 3)
	else:
	    a = a
	for i in range((a // 2)):
	    sstring.append('1')
	global_list.append(sstring)
	return global_list