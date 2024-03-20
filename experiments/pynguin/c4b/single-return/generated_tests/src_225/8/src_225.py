def func(*args):
	
	x = list(map(int, args[0].split()))
	t = len(x)
	m = len(set(x))
	return((t - m))
