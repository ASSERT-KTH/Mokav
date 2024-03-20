def func(*args):
	
	import math
	
	def is_prime(n):
	    if (n == 2):
	        return True
	    for i in range(2, (int(math.sqrt(n)) + 2)):
	        if ((n % i) == 0):
	            return False
	    return True
	
	def tax(n):
	    if is_prime(n):
	        return 1
	    if ((n % 2) == 0):
	        return 2
	    if is_prime((n - 2)):
	        return 2
	    return 3
	return(tax(int(args[0])))
