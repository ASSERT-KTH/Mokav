def func(*args):
	ret_values = []
	
	s = args[0]
	h = 0
	for i in range(0, len(s)):
	    if ((s[i] is 'H') or (s[i] is 'Q') or (s[i] is '9')):
	        ret_values.append('YES')
	        h = 1
	        break
	if (h is 0):
	    ret_values.append('NO')

	return ret_values
