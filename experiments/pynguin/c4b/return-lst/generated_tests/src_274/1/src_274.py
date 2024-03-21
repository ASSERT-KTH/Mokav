def func(*args):
	ret_values = []
	
	(a, b) = args[0].split()
	(a, b) = (int(a), int(b))
	if ((abs((a - b)) > 1) or ((a == 0) and (b == 0))):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
