def func(*args):
	ret_values = []
	
	s = args[0]
	while (s.find('//') != (- 1)):
	    s = s.replace('//', '/')
	if ((len(s) > 1) and (s[(- 1)] == '/')):
	    s = s[:(- 1)]
	ret_values.append(s)

	return ret_values
