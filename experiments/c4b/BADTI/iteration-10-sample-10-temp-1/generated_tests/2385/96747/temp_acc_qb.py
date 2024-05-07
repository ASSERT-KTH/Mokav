def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((- 128) <= n <= 127):
	    global_list.append('byte')
	elif ((- 32768) <= n <= 32767):
	    global_list.append('short')
	elif ((- 2147483648) <= n <= 2147483647):
	    global_list.append('int')
	elif ((- 9223372036854775808) <= n <= 9223372036854775807):
	    global_list.append('long')
	else:
	    global_list.append('BigInteger')
	return global_list