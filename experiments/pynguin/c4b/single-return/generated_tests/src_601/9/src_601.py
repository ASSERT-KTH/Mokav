def func(*args):
	
	(x, y) = map(int, args[0].split())
	(a, v) = (([y] * 3), 0)
	while (a[0] < x):
	    a[0] = min(x, ((a[1] + a[2]) - 1))
	    a.sort()
	    v += 1
	return(v)
