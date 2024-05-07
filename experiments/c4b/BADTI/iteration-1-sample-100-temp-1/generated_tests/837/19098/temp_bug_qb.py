def original_func(*args):
	global_list = []
	
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
	    return (tax((n - 3)) + 1)
	global_list.append(tax(int(args[0])))
	return global_list