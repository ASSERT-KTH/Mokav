def func(*args):
	ret_values = []
	
	
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
	while (0 < gcd(a[step], a[2]) <= a[2]):
	    a[2] = (a[2] - gcd(a[step], a[2]))
	    step = (1 - step)
	ret_values.append((1 - step))

	return ret_values
