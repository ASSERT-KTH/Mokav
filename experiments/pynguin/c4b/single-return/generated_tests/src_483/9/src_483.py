def func(*args):
	
	l = [int(i) for i in args[0].split()]
	l.sort()
	return(((l[1] - l[0]) + (l[2] - l[1])))
