def func(*args):
	
	(a, b) = map(int, args[0].split())
	x = 1
	while (0 != ((a * x) % 10) != b):
	    x = (x + 1)
	return(x)
