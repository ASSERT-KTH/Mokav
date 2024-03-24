def func(*args):
	ret_values = []
	
	a = int(args[0])
	if ((a % 2) == 0):
	    if (a == 2):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
