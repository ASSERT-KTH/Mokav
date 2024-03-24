def func(*args):
	
	f = [1, 1]
	n = int(args[0])
	i = 0
	while ((f[0] + f[1]) <= n):
	    i += 1
	    (f[0], f[1]) = (f[1], (f[0] + f[1]))
	return(i)
