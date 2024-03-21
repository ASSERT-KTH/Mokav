def func(*args):
	ret_values = []
	
	(t, s, x) = (int(z) for z in args[0].split())
	x -= t
	if ((x >= 0) and ((x % s) in [0, 1]) and (x != 1)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
