def func(*args):
	ret_values = []
	
	ret_values.append(('YES' if any(((c in 'HQ9') for c in args[0])) else 'NO'))

	return ret_values
