def original_func(*args):
	global_list = []
	
	import re
	reg = re.compile('(h)+(e)+(l)+(l)+(o)+')
	s1 = args[0]
	li = reg.findall(s1)
	if (not li):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list