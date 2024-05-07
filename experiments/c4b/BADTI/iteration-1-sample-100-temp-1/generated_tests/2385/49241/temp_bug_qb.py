def original_func(*args):
	global_list = []
	
	x = int(args[0])
	if (x <= 128):
	    global_list.append('byte')
	elif (x <= 32768):
	    global_list.append('short')
	elif (x <= 2147483648):
	    global_list.append('int')
	elif (x <= 9223372036854775808):
	    global_list.append('long')
	else:
	    global_list.append('BigInteger')
	return global_list