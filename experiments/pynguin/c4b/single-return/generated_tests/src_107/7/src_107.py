def func(*args):
	
	a = [int(x) for x in args[0].split(' ')]
	a.sort()
	dist = (a[2] - a[0])
	return(dist)
