def func(*args):
	
	s = args[0]
	a = s.split()
	n = int(a[0])
	b = int(a[1])
	p = int(a[2])
	t = n
	c = 1
	sm = 0
	while (n != 1):
	    while True:
	        if ((c * 2) > n):
	            break
	        c *= 2
	    sm = ((sm + (c // 2)) + (c * b))
	    n -= (c // 2)
	    c = 1
	return(sm, (t * p), end=' ')
