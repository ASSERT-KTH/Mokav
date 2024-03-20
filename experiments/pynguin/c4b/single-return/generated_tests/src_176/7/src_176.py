def func(*args):
	
	l = list(map(int, args[0].split()))
	l.sort()
	return((l[2] - l[0]))
