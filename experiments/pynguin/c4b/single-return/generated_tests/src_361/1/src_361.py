def func(*args):
	
	a = list(map(int, args[0].strip().split(' ')))
	a = sorted(a)
	d = (a[2] - a[0])
	return(d)
