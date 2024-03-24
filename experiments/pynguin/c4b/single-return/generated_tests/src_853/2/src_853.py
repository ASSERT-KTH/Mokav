def func(*args):
	
	a = list(map(int, args[0].split()))
	return((4 - len(set(a))))
