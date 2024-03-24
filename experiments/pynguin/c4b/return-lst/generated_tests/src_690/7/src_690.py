def func(*args):
	ret_values = []
	
	n = int(args[0])
	p = ((9 ** n) * (3 ** n))
	ret_values.append(((p - (7 ** n)) % 1000000007))

	return ret_values
