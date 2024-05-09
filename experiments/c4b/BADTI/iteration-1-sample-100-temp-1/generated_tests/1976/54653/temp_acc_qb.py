def patched_func(*args):
	global_list = []
	
	import re
	s = args[0]
	s = args[1]
	l = 0
	a = 0
	for i in range(len(s)):
	    if ((i == 0) or (s[(i - 1)] != s[i])):
	        a += l
	        l = 0
	    else:
	        l += 1
	global_list.append((a + l))
	return global_list