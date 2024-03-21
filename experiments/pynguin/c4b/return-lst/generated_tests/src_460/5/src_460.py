def func(*args):
	ret_values = []
	
	a = args[0]
	ret_values.append(['YES', 'NO'][all(((len(set(a[(i - 7):i])) > 1) for i in range(7, (len(a) + 1))))])

	return ret_values
