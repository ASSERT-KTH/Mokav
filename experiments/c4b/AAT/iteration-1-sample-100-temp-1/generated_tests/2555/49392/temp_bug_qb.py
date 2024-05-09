def original_func(*args):
	global_list = []
	
	str = args[0]
	zeros = '0000000'
	ones = '1111111'
	if ((str in zeros) or (str in ones)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list