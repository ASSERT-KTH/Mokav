def func(*args):
	ret_values = []
	
	n = int(args[0])
	mod = 1000000007
	ret_values.append((int(((pow(3, n, (4 * mod)) + (3 * ((- 1) ** n))) / 4)) % (4 * mod)))

	return ret_values
