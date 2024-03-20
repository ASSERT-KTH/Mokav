def func(*args):
	
	(a, b) = map(int, args[0].split())
	b = ((240 - b) // 5)
	i = 0
	while ((i < a) and (b >= 0)):
	    i += 1
	    b -= i
	return((i - (b < 0)))
