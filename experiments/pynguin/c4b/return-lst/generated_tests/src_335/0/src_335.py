def func(*args):
	ret_values = []
	
	a = args[0]
	f = 0
	for i in a:
	    if ((i == 'H') or (i == 'Q') or (i == '9')):
	        f = 1
	        ret_values.append('YES')
	        break
	if (f == 0):
	    ret_values.append('NO')

	return ret_values
