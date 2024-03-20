def func(*args):
	
	
	def compute():
	    (a, b) = map(int, args[0].split())
	    if ((a == 0) and (b == 0)):
	        return 'NO'
	    if (abs((a - b)) <= 1):
	        return 'YES'
	    else:
	        return 'NO'
	return(compute())
