def func(*args):
	
	a = int(args[0])
	
	def f(a):
	    if (((a % 2) == 0) and (a != 2)):
	        return 'YES'
	    return 'NO'
	return(f(a))
