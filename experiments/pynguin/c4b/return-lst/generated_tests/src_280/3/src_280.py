def func(*args):
	ret_values = []
	
	A = args[0]
	a = 0
	for i in A:
	    if ((i == 'H') or (i == 'Q') or (i == '9')):
	        ret_values.append('YES')
	        a = 1
	        break
	if (a == 0):
	    ret_values.append('NO')

	return ret_values
