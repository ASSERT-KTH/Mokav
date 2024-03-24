def func(*args):
	ret_values = []
	
	n = int(args[0])
	if (((n % 4) == 0) or ((n % 7) == 0) or ((n % 47) == 0) or ((n % 74) == 0) or ((n % 444) == 0) or ((n % 447) == 0) or ((n % 477) == 0) or ((n % 744) == 0) or ((n % 774) == 0) or ((n % 777) == 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
