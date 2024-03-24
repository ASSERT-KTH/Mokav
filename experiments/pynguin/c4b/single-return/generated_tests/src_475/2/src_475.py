def func(*args):
	
	i = list(map(int, args[0].split()))
	return((max(i) - min(i)))
