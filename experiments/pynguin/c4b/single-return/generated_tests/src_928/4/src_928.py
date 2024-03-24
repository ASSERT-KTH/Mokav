def func(*args):
	
	n = int(args[0])
	output = ((n // 3) * 2)
	return(((output + 1) if ((n % 3) > 0) else output))
