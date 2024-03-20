def func(*args):
	
	s = args[0]
	while (s.find('//') != (- 1)):
	    s = s.replace('//', '/')
	if ((len(s) > 1) and (s[(- 1)] == '/')):
	    s = s[:(- 1)]
	return(s)
