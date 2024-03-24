def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 4) and (n % 7) and (n % 47) and (n % 74) and (n % 447) and (n % 474) and (n % 477) and (n % 744) and (n % 747) and (n % 774)):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
