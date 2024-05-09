def original_func(*args):
	global_list = []
	
	import re
	s = args[0]
	s = args[1]
	l = len(s)
	s *= 1000
	a = 0
	for i in range(l):
	    try:
	        if ((s[(i + 1)] == s[i]) or (s[(i - 1)] == s[i])):
	            a += 1
	            try:
	                if ((s[i] != s[(i - 1)]) and (s[(i - 2)] == s[(i - 1)])):
	                    a -= 1
	            except:
	                pass
	    except:
	        if (s[(i + 1)] == s[i]):
	            a += 1
	if (a == 0):
	    a += 1
	global_list.append((a - 1))
	return global_list