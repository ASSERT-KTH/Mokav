def func(*args):
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	while (((a * 4) > c) or ((a * 2) > b)):
	    a = (a - 1)
	return(((a + (a * 2)) + (a * 4)))
