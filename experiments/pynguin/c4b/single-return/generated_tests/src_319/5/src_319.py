def func(*args):
	
	a = list(map(int, args[0].split()))
	return((max(a) - min(a)))
