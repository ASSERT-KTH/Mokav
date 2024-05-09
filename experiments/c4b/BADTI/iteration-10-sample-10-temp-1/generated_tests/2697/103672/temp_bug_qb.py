def original_func(*args):
	global_list = []
	
	
	def ext_gcd(a, b):
	    if (a == 0):
	        return (b, 0, 1)
	    else:
	        (g, x, y) = ext_gcd((b % a), a)
	        return (g, (y - ((b // a) * x)), x)
	(a, b) = map(int, args[0].split(' '))
	(c, d) = map(int, args[1].split(' '))
	min = (- 1)
	for i in range(110):
	    if (((b + (i * a)) % c) == (d % c)):
	        if ((min == (- 1)) or (min > (b + (i * a)))):
	            min = (b + (i * a))
	    if (((d + (i * c)) % a) == (b % a)):
	        if ((min == (- 1)) or (min > (d + (i * c)))):
	            min = (d + (i * c))
	global_list.append(min)
	return global_list