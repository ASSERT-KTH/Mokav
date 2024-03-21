def func(*args):
	ret_values = []
	
	(t, s, x) = map(int, args[0].split())
	if (x < t):
	    ret_values.append('NO')
	    exit()
	if ((x == t) or (((x - t) % s) == 0) or (((((x - t) - 1) % s) == 0) and ((((x - t) - 1) // s) >= 1))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
