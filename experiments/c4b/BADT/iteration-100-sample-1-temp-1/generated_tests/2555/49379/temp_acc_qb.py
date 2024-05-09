def patched_func(*args):
	global_list = []
	
	s = args[0]
	zeros = '0000000'
	ones = '1111111'
	if ((zeros in s) | (ones in s)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list