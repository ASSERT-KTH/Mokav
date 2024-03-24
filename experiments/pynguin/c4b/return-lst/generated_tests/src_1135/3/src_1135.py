def func(*args):
	ret_values = []
	
	(t, s, x) = [int(x) for x in args[0].split()]
	if ((((((x - t) % s) == 0) or ((((x - t) - 1) % s) == 0)) and (x >= (t + s))) or (x == t)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
