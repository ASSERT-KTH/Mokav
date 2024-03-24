def func(*args):
	
	
	def fact(n):
	    res = 1
	    for i in range(2, (n + 1)):
	        res = ((res * i) % ((10 ** 9) + 7))
	    return res
	
	def rev(a):
	    return pow(a, ((10 ** 9) + 5), ((10 ** 9) + 7))
	
	def c2nn(n):
	    return ((fact((2 * n)) * (rev(fact(n)) ** 2)) % ((10 ** 9) + 7))
	n = int(args[0])
	return((c2nn(n) - n))
