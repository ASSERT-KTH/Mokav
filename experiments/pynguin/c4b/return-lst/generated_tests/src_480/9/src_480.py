def func(*args):
	ret_values = []
	
	table = ['1/1', '5/6', '2/3', '1/2', '1/3', '1/6']
	(a, b) = map(int, args[0].split())
	ret_values.append(table[(max(a, b) - 1)])

	return ret_values
