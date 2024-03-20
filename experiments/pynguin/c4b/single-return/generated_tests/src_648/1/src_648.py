def func(*args):
	
	(*l, a, b) = map(int, args[0].split())
	return(max(0, (min((b + 1), *l) - a)))
