def func(*args):
	
	(a, b, n) = [int(x) for x in args[0].split(' ')]
	
	def addingdigits(a, b, n):
	    t = 0
	    for i in range(10):
	        if ((((a * 10) + i) % b) == 0):
	            t = ((a * 10) + i)
	            break
	    if (t == 0):
	        return (- 1)
	    else:
	        return (t * pow(10, (n - 1)))
	return(addingdigits(a, b, n))
