def func(*args):
	ret_values = []
	
	n = args[0]
	years = [int(s) for s in args[1].split()]
	ret_values.append((sum(years) // int(n)))

	return ret_values
