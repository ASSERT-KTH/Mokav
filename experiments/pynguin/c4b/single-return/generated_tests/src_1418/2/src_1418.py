def func(*args):
	
	
	def mcd(a, b):
	    resto = 0
	    while (b > 0):
	        resto = b
	        b = (a % b)
	        a = resto
	    return a
	n = int(args[0])
	y = n
	k = 2
	p = 0
	r = 0
	for q in range(0, (n - 2)):
	    n = y
	    while (n >= k):
	        a = (n % k)
	        p = (p + a)
	        n = (n // k)
	    p = (p + n)
	    k = (k + 1)
	t = (k - 2)
	a = mcd(p, t)
	nu = (p // a)
	de = (t // a)
	return(((str(nu) + '/') + str(de)))
