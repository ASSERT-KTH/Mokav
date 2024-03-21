def func(*args):
	ret_values = []
	
	(t, s, x) = map(int, args[0].split())
	if ((((x % s) == (t % s)) and (t <= x)) or (((x % s) == ((t + 1) % s)) and ((t + 1) < x))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
