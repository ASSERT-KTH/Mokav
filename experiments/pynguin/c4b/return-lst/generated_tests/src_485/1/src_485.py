def func(*args):
	ret_values = []
	
	(a, b) = (int(i) for i in args[0].split())
	ret_values.append(('YES' if ((abs((a - b)) <= 1) and ((a + b) > 0)) else 'NO'))

	return ret_values
