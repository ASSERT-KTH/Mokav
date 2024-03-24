def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].strip().split())
	if ((abs((a - b)) < 2) and ((a + b) != 0)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
