def func(*args):
	ret_values = []
	
	p = args[0]
	for i in range(len(p)):
	    if ((p[i] == 'H') or (p[i] == 'Q') or (p[i] == '9')):
	        ret_values.append('YES')
	        exit(0)
	ret_values.append('NO')

	return ret_values
