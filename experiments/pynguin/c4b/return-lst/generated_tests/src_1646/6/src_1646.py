def func(*args):
	ret_values = []
	
	from decimal import *
	n = Decimal(args[0])
	ret_values.append(int(((((0 + (n * 6)) * (n + 1)) / 2) + 1)))

	return ret_values
