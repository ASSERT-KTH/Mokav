def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	if ((max(n, m) - min(n, m)) in {0, 1}):
	    if ((n == 0) and (m == 0)):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
