def func(*args):
	ret_values = []
	
	(t, s, x) = map(int, args[0].split())
	c = 0
	if (((x - t) < 0) or (((s - t) > x) and ((x - t) != 0))):
	    c = 1
	if (((((x - t) % s) == 0) and (c == 0)) or (((((x - t) - 1) % s) == 0) and (c == 0) and (((x - t) - 1) != 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
