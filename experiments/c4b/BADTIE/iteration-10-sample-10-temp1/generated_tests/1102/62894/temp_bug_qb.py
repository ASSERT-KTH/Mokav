def original_func(*args):
	global_list = []
	
	s = args[0].lower()
	s2 = ''
	v = 'aoyeui'
	i = 0
	while (i < len(s)):
	    if (s[i] in v):
	        s2 += '.'
	    else:
	        s2 += s[i]
	    i += 1
	global_list.append(s2)
	return global_list