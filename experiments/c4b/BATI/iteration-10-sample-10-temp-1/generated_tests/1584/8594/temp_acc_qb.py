def patched_func(*args):
	global_list = []
	
	s = args[0]
	while (s.find('//') != (- 1)):
	    s = s.replace('//', '/')
	if ((len(s) > 1) and (s[(- 1)] == '/')):
	    s = s[:(- 1)]
	global_list.append(s)
	return global_list