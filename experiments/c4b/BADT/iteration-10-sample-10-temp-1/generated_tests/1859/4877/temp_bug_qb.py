def original_func(*args):
	global_list = []
	
	s = args[0]
	if (s[0:3] == 'ftp'):
	    s = s.replace('ftp', 'ftp://', 1)
	else:
	    s = s.replace('http', 'http://', 1)
	s = s.replace('ru', '.ru/', 1)
	if (s[(- 1)] == '/'):
	    global_list.append(s[0:(- 1)])
	else:
	    global_list.append(s)
	return global_list