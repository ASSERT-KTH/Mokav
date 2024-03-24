def func(*args):
	
	n = int(args[0])
	R = (lambda : map(int, args[1].split()))
	l = list(R())
	l.sort()
	return(l[((n - 1) // 2)])
