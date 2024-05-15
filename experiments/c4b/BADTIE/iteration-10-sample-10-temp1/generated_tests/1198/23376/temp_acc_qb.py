def patched_func(*args):
	global_list = []
	
	s = args[0]
	a = []
	for i in range(len(s)):
	    a.append(s[i])
	if (('H' in a) or ('Q' in a) or ('9' in a)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list