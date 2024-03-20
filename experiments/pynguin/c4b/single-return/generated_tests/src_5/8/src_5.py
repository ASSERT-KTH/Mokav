def func(*args):
	
	
	def pow(x, k):
	    if (k == 0):
	        return 1
	    a = pow(x, int((k / 2)))
	    a = (a * a)
	    if ((k % 2) == 1):
	        a = (a * x)
	    a = (a % 10)
	    return int(a)
	a = int(args[0].strip())
	return(pow(1378, a))
