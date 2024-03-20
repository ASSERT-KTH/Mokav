def func(*args):
	
	(k, a, b) = args[0].split(' ')
	k = int(k)
	a = int(a)
	b = int(b)
	if ((a % k) != 0):
	    a = ((a + k) - (a % k))
	return(max(0, (1 + ((b - a) // k))))
