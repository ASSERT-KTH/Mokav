def func(*args):
	ret_values = []
	
	n = int(args[0])
	mod = ((10 ** 9) + 7)
	x = (((3 * ((- 1) ** n)) + pow(3, n, (mod * 4))) * (1 / 4))
	ret_values.append(int(x))

	return ret_values
