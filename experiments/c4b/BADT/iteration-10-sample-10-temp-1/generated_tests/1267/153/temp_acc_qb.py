def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	s = args[1]
	k = ((s[:(n // 2)].count('4') * 4) + (s[:(n // 2)].count('7') * 7))
	l = ((s[(n // 2):].count('4') * 4) + (s[(n // 2):].count('7') * 7))
	if (((n % 2) == 0) and ((s.count('4') + s.count('7')) == n) and (k == l)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list