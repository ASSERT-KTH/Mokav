def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	if ((n == m) and (n != 0) and (m != 0)):
	    ret_values.append('YES')
	elif (((n + 1) == m) or ((n - 1) == m)):
	    ret_values.append('YES')
	elif ((n == 0) and (m == 0)):
	    ret_values.append('NO')
	else:
	    ret_values.append('NO')

	return ret_values
