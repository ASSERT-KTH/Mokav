def func(*args):
	
	l = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = int(args[0].strip())
	i = 1
	while ((i * 5) < n):
	    n -= (i * 5)
	    i *= 2
	return(l[((n - 1) // i)])
