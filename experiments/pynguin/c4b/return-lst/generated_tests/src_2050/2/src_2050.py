def func(*args):
	ret_values = []
	
	(a, b) = args[0].split()
	a = int(a)
	b = int(b)
	if ((abs((a - b)) > 1) or ((not a) and (not b))):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
