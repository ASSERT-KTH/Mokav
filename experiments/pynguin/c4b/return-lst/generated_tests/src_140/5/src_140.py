def func(*args):
	ret_values = []
	
	'input\n3 10 4\n'
	(t, s, x) = map(int, args[0].split())
	if (((((x - t) % s) == 0) or ((((x - t) - 1) % s) == 0)) and ((x - t) != 1) and ((x - t) >= 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
