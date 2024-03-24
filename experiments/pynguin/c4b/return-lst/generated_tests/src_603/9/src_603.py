def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	ret_values.append(('YES' if ((abs((a - b)) <= 1) and (max(a, b) > 0)) else 'NO'))

	return ret_values
