def func(*args):
	ret_values = []
	
	p = str(args[0])
	for i in range(0, len(p)):
	    if ((p[i] == 'H') or (p[i] == 'Q') or (p[i] == '9')):
	        ret_values.append('YES')
	        break
	else:
	    ret_values.append('NO')

	return ret_values
