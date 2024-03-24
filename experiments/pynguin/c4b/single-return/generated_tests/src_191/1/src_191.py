def func(*args):
	
	(a, b) = map(int, args[0].split())
	return(min(a, b), (abs((a - b)) // 2))
