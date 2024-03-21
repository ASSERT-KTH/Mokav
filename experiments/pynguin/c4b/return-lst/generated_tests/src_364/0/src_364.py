def func(*args):
	ret_values = []
	
	
	def gcd(a, b):
	    if (b == 0):
	        return a
	    else:
	        return gcd(b, (a % b))
	(a, b, n) = map(int, args[0].split())
	count = 0
	while (1 < 2):
	    if (n == 0):
	        ret_values.append((1 - int((count % 2))))
	        break
	    elif ((count % 2) == 0):
	        n -= gcd(n, a)
	        count += 1
	    else:
	        n -= gcd(n, b)
	        count += 1

	return ret_values
