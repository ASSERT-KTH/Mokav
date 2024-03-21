def func(*args):
	ret_values = []
	
	s = args[0]
	c = 1
	i = 1
	t = s[0]
	while ((c != 7) and (i < len(s))):
	    if (s[i] == t):
	        c += 1
	    else:
	        t = s[i]
	        c = 1
	    i += 1
	if (c == 7):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
