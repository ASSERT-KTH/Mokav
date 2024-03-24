def func(*args):
	
	n = int(args[0])
	
	def S(x):
	    if (x > n):
	        return 0
	    return ((1 + S((x * 10))) + S(((x * 10) + 1)))
	return(S(1))
