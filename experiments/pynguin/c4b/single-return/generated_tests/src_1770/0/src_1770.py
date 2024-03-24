def func(*args):
	
	n = int(args[0])
	a = (2 ** n)
	if (n >= 13):
	    a -= ((2 ** (n - 13)) * 100)
	return(a)
