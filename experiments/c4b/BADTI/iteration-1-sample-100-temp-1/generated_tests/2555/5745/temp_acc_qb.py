def patched_func(*args):
	global_list = []
	
	s = str(args[0])
	(chk1, chk2) = ('0000000', '1111111')
	if ((s.find(chk1) >= 0) or (s.find(chk2) >= 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list