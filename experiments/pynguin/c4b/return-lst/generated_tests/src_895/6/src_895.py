def func(*args):
	ret_values = []
	
	p = args[0]
	i = 0
	while (i < len(p)):
	    if ((p[i] == 'H') or (p[i] == 'Q') or (p[i] == '9')):
	        ret_values.append('YES')
	        break
	    i += 1
	else:
	    ret_values.append('NO')

	return ret_values
