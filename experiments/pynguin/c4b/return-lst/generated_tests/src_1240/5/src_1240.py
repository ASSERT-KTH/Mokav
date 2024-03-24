def func(*args):
	ret_values = []
	
	(a, b, n) = map(int, args[0].split())
	
	def gcd(a, b):
	    if (b != 0):
	        return gcd(b, (a % b))
	    else:
	        return a
	i = 0
	while 1:
	    if ((i % 2) == 0):
	        s = gcd(a, n)
	        n = (n - s)
	    else:
	        s = gcd(b, n)
	        n = (n - s)
	    i += 1
	    if (n == 0):
	        break
	if ((i % 2) == 0):
	    ret_values.append(1)
	else:
	    ret_values.append(0)

	return ret_values
