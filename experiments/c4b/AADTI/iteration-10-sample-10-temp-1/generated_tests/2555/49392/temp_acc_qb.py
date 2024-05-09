def patched_func(*args):
	global_list = []
	
	str = args[0]
	zeros = '0000000'
	ones = '1111111'
	if ((zeros in str) or (ones in str)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list