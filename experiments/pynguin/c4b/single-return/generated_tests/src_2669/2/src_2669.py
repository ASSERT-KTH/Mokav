def func(*args):
	
	
	def fact(n):
	    b = ([0] * (n + 1))
	    b[1] = 1
	    for i in range(2, (n + 1)):
	        b[i] = (i * b[(i - 1)])
	    return b[n]
	(n, k) = map(int, args[0].split(' '))
	a = min(n, k)
	return(fact(a))
