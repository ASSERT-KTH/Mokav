def func(*args):
	ret_values = []
	
	(t, s, x) = map(int, args[0].split())
	if (x < t):
	    ret_values.append('NO')
	elif ((((x - t) % s) == 0) or ((((x - 1) - t) % s) == 0)):
	    if (x == (t + 1)):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
