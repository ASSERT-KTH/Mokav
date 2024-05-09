def original_func(*args):
	global_list = []
	
	s = args[0]
	ans = ''
	l = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	for i in s:
	    if (i not in l):
	        ans = ((ans + '.') + i.lower())
	global_list.append(ans)
	return global_list