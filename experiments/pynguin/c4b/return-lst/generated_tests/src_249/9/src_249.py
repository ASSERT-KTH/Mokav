def func(*args):
	ret_values = []
	
	n = int(args[0])
	m = 1
	nms = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	while ((m * 5) < n):
	    n -= (m * 5)
	    m *= 2
	ret_values.append(nms[((n - 1) // m)])

	return ret_values
