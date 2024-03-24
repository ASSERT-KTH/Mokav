def func(*args):
	
	n = int(args[0])
	e = (10 ** 9)
	a = e
	b = e
	for i in range((n // 3), (- 1), (- 1)):
	    x = ((n - (i * 4)) // 7)
	    if ((x >= 0) and (((x * 7) + (i * 4)) == n) and (((a + b) > (i + x)) or (b > x))):
	        (a, b) = (i, x)
	return(((- 1) if (a == e) else (('4' * a) + ('7' * b))))
