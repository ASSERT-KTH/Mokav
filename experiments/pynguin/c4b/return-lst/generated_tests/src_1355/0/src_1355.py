def func(*args):
	ret_values = []
	
	a = list(args[0].split())
	a[0] = int(a[0])
	a[1] = int(a[1])
	stos = int(a[2])
	
	def gcd(x, y):
	    while y:
	        (x, y) = (y, (x % y))
	    return x
	res = False
	while True:
	    t = gcd(a[res], stos)
	    if ((stos - t) < 0):
	        ret_values.append(int((not res)))
	        break
	    else:
	        stos -= t
	    res = (not res)

	return ret_values
