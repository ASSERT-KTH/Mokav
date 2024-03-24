def func(*args):
	ret_values = []
	
	(p, n) = args[0].split()
	p = int(p)
	n = int(n)
	if ((p == 0) and (n == 0)):
	    ret_values.append('NO')
	elif ((p == n) or ((n - p) == 1) or ((p - n) == 1)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
