def func(*args):
	
	(c, a, b) = map(int, args[0].split())
	if ((a % c) == 0):
	    d = ((int((b // c)) - int((a // c))) + 1)
	else:
	    d = (int((b // c)) - int((a // c)))
	return(d)
