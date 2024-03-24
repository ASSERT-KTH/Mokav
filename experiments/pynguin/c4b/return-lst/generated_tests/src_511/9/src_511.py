def func(*args):
	ret_values = []
	
	(n, k) = [int(i) for i in args[0].split()]
	if (abs((n - k)) <= 1):
	    if (n == k == 0):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
