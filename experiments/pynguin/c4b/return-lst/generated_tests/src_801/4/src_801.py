def func(*args):
	ret_values = []
	
	
	def gcd(a, b):
	    while ((a != 0) and (b != 0)):
	        if (a > b):
	            a = (a - b)
	        else:
	            b = (b - a)
	    return max(a, b)
	(a, b, n) = map(int, args[0].split())
	x = 0
	if ((a == 1) and (b == 1)):
	    if ((n % 2) == 0):
	        ret_values.append(1)
	    else:
	        ret_values.append(0)
	else:
	    while (n > 0):
	        if (x == 0):
	            n = (n - gcd(n, a))
	            x += 1
	        else:
	            n = (n - gcd(n, b))
	            x -= 1
	    else:
	        if x:
	            ret_values.append((x - 1))
	        else:
	            ret_values.append((x + 1))

	return ret_values
