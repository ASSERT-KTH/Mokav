def func(*args):
	
	(x, y) = args[0].split()
	number_of_dominos = int(((int(x) * int(y)) / 2))
	return(number_of_dominos)
