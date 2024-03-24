def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	if (n > m):
	    a = (n - m)
	else:
	    a = (m - n)
	if (a > 1):
	    ret_values.append('NO')
	elif ((a == 0) and ((m == 0) or (n == 0))):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
