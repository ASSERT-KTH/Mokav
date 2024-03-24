def func(*args):
	
	n = int(args[0])
	p = list(map(int, args[1].split()))
	c = 0
	i = 0
	while (c < n):
	    c += p[i]
	    i = ((i + 1) % 7)
	if (i == 0):
	    i = 7
	return(i)
