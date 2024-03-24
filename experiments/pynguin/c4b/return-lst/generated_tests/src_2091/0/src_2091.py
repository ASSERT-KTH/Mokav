def func(*args):
	ret_values = []
	
	number = int(args[0])
	if (number == 2):
	    ret_values.append('NO')
	elif ((number % 2) == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
