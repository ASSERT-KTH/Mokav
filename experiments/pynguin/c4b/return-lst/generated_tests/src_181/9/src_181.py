def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	if ((abs((a - b)) <= 1) and (not ((b == 0) and (a == 0)))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
