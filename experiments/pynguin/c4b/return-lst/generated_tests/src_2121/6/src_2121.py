def func(*args):
	ret_values = []
	
	line = args[0]
	for i in line:
	    if ((i == 'H') or (i == 'Q') or (i == '9')):
	        ret_values.append('YES')
	        break
	else:
	    ret_values.append('NO')

	return ret_values
