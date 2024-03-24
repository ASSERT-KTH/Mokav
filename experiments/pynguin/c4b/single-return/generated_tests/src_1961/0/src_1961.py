def func(*args):
	
	(a, b) = args[0].split(' ')
	a = int(a)
	b = int(b)
	c = 1
	while ((((a * c) % 10) != b) and (((a * c) % 10) != 0)):
	    c = (c + 1)
	return(c)
