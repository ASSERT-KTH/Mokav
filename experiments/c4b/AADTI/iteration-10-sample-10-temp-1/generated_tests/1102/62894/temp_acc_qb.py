def patched_func(*args):
	global_list = []
	
	s = args[0].lower()
	s2 = '.'
	v = 'aoyeui'
	i = 0
	while (i < len(s)):
	    if (not (s[i] in v)):
	        s2 += s[i]
	        s2 += '.'
	    i += 1
	i = 0
	s = ''
	while (i < (len(s2) - 1)):
	    s += s2[i]
	    i += 1
	global_list.append(s)
	return global_list