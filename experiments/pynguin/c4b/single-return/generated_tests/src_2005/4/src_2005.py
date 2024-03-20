def func(*args):
	
	a = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = (int(args[0]) - 1)
	i = 5
	while (n >= i):
	    n -= i
	    i *= 2
	p = int((n / (i / 5)))
	return(a[p])
