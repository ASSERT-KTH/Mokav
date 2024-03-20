def func(*args):
	
	x = int(args[0])
	y = ((x // 5) + ((x % 5) != 0))
	return(y)
