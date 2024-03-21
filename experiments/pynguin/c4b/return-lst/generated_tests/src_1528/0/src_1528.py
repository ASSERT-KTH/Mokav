def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n == 447) or (n == 774) or (n == 477) or (n == 477)):
	    ret_values.append('YES')
	elif (((n % 4) == 0) or ((n % 7) == 0) or ((n % 74) == 0) or ((n % 47) == 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
