def func(*args):
	ret_values = []
	
	(t, s, x) = list(map(int, args[0].split()))
	if (x < t):
	    ret_values.append('NO')
	else:
	    x -= t
	    if (x == 1):
	        ret_values.append('NO')
	    elif (((x % s) == 0) or ((x % s) == 1)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
