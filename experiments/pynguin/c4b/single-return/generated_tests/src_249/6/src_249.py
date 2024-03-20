def func(*args):
	
	n = int(args[0])
	m = 1
	nms = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	while ((m * 5) < n):
	    n -= (m * 5)
	    m *= 2
	return(nms[((n - 1) // m)])
