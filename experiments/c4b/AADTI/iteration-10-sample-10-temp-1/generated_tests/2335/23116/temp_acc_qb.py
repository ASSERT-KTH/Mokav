def patched_func(*args):
	global_list = []
	
	import re
	reg = re.compile('(h)+[a-z]*(e)+[a-z]*(l)+[a-z]*(l)+[a-z]*(o)+[a-z]*')
	s1 = args[0]
	li = reg.findall(s1)
	if (not li):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list