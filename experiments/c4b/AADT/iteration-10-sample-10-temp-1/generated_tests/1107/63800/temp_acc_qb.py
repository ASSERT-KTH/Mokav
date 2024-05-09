def patched_func(*args):
	global_list = []
	
	x = [int(i) for i in args[0].split()]
	(a, b, n) = (x[0], x[1], x[2])
	
	def gcd(a, b):
	    if ((a * b) == 0):
	        if (a == 0):
	            return b
	        else:
	            return a
	    elif (a > b):
	        while ((a % b) != 0):
	            a = (a % b)
	            c = a
	            a = b
	            b = c
	        return b
	    else:
	        c = a
	        a = b
	        b = c
	        while ((a % b) != 0):
	            a = (a % b)
	            c = a
	            a = b
	            b = c
	        return b
	t = 0
	while True:
	    if (t == 0):
	        if (n < gcd(a, n)):
	            break
	        n = (n - gcd(a, n))
	        t = 1
	    elif (t == 1):
	        if (n < gcd(b, n)):
	            break
	        n = (n - gcd(b, n))
	        t = 0
	global_list.append((1 - t))
	return global_list