def func(*args):
	
	(n, m) = map(int, args[0].split())
	l = ((m + n) - 3)
	if (((m - n) % 3) != 0):
	    l += 1
	return(max(l, 0))
