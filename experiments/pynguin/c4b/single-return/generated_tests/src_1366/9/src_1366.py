def func(*args):
	
	number = int(args[0])
	n = int(((1 + ((1 + (8 * (number - 1))) ** (1 / 2))) / 2))
	return((number - ((n * (n - 1)) // 2)))
