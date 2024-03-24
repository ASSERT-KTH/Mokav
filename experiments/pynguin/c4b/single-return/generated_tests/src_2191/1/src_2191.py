def func(*args):
	
	(n, t) = args[0].strip().split(' ')
	(n, t) = (int(n), int(t))
	s = args[1].strip()
	q = list(s)
	for _ in range(t):
	    i = 0
	    while (i < (len(q) - 1)):
	        if ((q[i] == 'B') and (q[(i + 1)] == 'G')):
	            (q[i], q[(i + 1)]) = (q[(i + 1)], q[i])
	            i = (i + 1)
	        i = (i + 1)
	return(''.join(q))
