def func(*args):
	ret_values = []
	
	import math
	(n, m) = map(int, args[0].split())
	c = n
	
	def IsPrime(x):
	    for i in range(2, (int(math.sqrt(x)) + 1)):
	        if ((x % i) == 0):
	            return False
	    return True
	while True:
	    c += 1
	    if IsPrime(c):
	        if (c == m):
	            ret_values.append('YES')
	            break
	        else:
	            ret_values.append('NO')
	            break

	return ret_values
