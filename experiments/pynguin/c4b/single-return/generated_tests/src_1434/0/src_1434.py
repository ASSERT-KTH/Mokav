def func(*args):
	
	
	def fact(x):
	    r = 1
	    for i in range(2, (x + 1)):
	        r = (r * i)
	    return r
	ch = args[0]
	l = ch.split(' ')
	a = int(l[0])
	b = int(l[1])
	return(fact(min(a, b)))
