def func(*args):
	ret_values = []
	
	
	def gcd(a, b):
	    if (a < b):
	        (a, b) = (b, a)
	    return (b if ((a % b) == 0) else gcd(b, (a % b)))
	(n, a, b) = map(int, args[0].split())
	k = ((a * b) // gcd(a, b))
	res = (((min(a, b) * (n // k)) + min(((n % k) + 1), min(a, b))) - 1)
	k = (n if (res == 0) else gcd(res, n))
	ret_values.append('{}/{}'.format((res // k), (n // k)))

	return ret_values
