def func(*args):
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	return(max(abs((a - c)), abs((d - b))))
