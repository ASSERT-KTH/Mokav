def func(*args):
	
	
	def bigyears(a, b):
	    n = 0
	    while (a <= b):
	        a = (a * 3)
	        b = (b * 2)
	        n = (n + 1)
	    return n
	(a, b) = args[0].split(' ')
	a = int(a)
	b = int(b)
	return(bigyears(a, b))
