def func(*args):
	
	x = list(map(int, args[0].strip().split()))
	return(abs((min(x) - max(x))))
