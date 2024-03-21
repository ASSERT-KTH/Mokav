def func(*args):
	ret_values = []
	
	a = args[0]
	a = int(a)
	if (((a % 2) == 0) and (a != 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
