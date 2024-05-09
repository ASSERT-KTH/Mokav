def original_func(*args):
	global_list = []
	
	s = str(args[0])
	if (('H' in s) or ('Q' in s) or ('9' in s) or ('+' in s)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list