def func(*args):
	
	x = args[0]
	if (x.isupper() or (x[0].islower() and x[1:len(x)].isupper()) or ((len(x) == 1) and x.islower())):
	    x = x.swapcase()
	return(x)
