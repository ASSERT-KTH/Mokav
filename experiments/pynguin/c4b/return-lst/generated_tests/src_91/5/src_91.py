def func(*args):
	ret_values = []
	
	s = args[0]
	l = 8
	h = 0
	if ((s[1] == '1') or (s[1] == '8')):
	    h = 1
	    l -= 3
	if ((s[0] == 'a') or (s[0] == 'h')):
	    if (h == 1):
	        l -= 2
	    else:
	        l -= 3
	ret_values.append(l)

	return ret_values
