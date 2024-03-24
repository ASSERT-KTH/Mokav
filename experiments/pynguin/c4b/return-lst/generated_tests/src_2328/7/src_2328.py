def func(*args):
	ret_values = []
	
	(x, y) = args[0].split()
	number_of_dominos = int(((int(x) * int(y)) / 2))
	ret_values.append(number_of_dominos)

	return ret_values
