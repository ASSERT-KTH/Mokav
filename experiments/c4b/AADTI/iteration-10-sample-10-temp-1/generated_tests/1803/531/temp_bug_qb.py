def original_func(*args):
	global_list = []
	
	'input\n8\n'
	from math import gcd
	
	def pf(n):
	    s = set()
	    while ((n % 2) == 0):
	        n //= 2
	        s.add(2)
	    for x in range(3, (int((n ** 0.5)) + 1), 2):
	        while ((n % x) == 0):
	            n //= x
	            s.add(x)
	    if (n > 1):
	        s.add(n)
	    return list(s)
	(n, m) = (int(args[0]), 0)
	if (n <= 3):
	    global_list.append([1, 2, 6][(n - 1)])
	elif ((n % 2) == 1):
	    global_list.append(((n * (n - 1)) * (n - 2)))
	else:
	    m = 0
	    for x in range(min((n - 2), 50)):
	        l = ((n * (n - 1)) // gcd(n, (n - 1)))
	        l = ((l * (n - 2)) // gcd(l, (n - 2)))
	        m = max(m, l)
	        n -= 1
	    global_list.append(m)
	return global_list