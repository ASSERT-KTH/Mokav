def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = args[1]
	if (((n % 2) == 0) and ((s.count('4') + s.count('7')) == n) and (int(s[:(n // 2)]) == int(s[(n // 2):]))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list