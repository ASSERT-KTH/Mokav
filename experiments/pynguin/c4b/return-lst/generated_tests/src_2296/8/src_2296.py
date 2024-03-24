def func(*args):
	ret_values = []
	
	s = args[0]
	for c in s:
	    if ((c == 'H') or (c == 'Q') or (c == '9')):
	        ret_values.append('YES')
	        quit()
	ret_values.append('NO')

	return ret_values
