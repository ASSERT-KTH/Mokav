def func(*args):
	ret_values = []
	
	(a, b) = [int(x) for x in args[0].split()]
	if ((abs((a - b)) not in [0, 1]) or ((a == 0) and (b == 0))):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
