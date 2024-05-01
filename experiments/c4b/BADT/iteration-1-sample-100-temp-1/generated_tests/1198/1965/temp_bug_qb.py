def original_func(*args):
	global_list = []
	
	inStr = args[0]
	found = False
	if (inStr.find('H') != (- 1)):
	    found = True
	if (inStr.find('Q') != (- 1)):
	    found = True
	if (inStr.find('9') != (- 1)):
	    found = True
	if (inStr.find('+') != (- 1)):
	    found = True
	if found:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list