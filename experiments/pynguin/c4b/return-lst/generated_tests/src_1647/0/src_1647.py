def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	if ((a == b) and (a == 0)):
	    ret_values.append('NO')
	else:
	    ret_values.append(('YES' if (abs((a - b)) <= 1) else 'NO'))

	return ret_values
