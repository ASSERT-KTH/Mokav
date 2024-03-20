def func(*args):
	
	[m, n, a] = map(int, args[0].split(' '))
	n1 = int((m / a))
	n2 = int((n / a))
	if ((m - (n1 * a)) > 0):
	    n1 = (n1 + 1)
	if ((n - (n2 * a)) > 0):
	    n2 = (n2 + 1)
	return((n1 * n2))
