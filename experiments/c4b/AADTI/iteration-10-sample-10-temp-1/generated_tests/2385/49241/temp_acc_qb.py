def patched_func(*args):
	global_list = []
	
	x = int(args[0])
	if (x <= 127):
	    global_list.append('byte')
	elif (x <= 32767):
	    global_list.append('short')
	elif (x <= 2147483647):
	    global_list.append('int')
	elif (x <= 9223372036854775807):
	    global_list.append('long')
	else:
	    global_list.append('BigInteger')
	return global_list