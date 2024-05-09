def original_func(*args):
	global_list = []
	
	
	def gcd(m, n):
	    if (m < n):
	        small = m
	    else:
	        small = n
	    for i in range((small + 1), 0, (- 1)):
	        if (((m % i) == 0) and ((n % i) == 0)):
	            return i
	a = [int(i) for i in args[0].split()]
	step = 0
	while (int(gcd(a[step], a[2])) <= a[2]):
	    step = (1 - step)
	    a[2] = (a[2] - gcd(a[step], a[2]))
	global_list.append(step)
	return global_list