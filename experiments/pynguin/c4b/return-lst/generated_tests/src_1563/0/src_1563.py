def func(*args):
	ret_values = []
	
	from sys import stdin
	(a, b, n) = (int(x) for x in stdin.readline().strip().split(' '))
	
	def gcd(a, b):
	    if (b == 0):
	        return a
	    return gcd(b, (a % b))
	while True:
	    take = gcd(a, n)
	    if (n < take):
	        ret_values.append(1)
	        break
	    n -= take
	    take = gcd(b, n)
	    if (n < take):
	        ret_values.append(0)
	        break
	    n -= take

	return ret_values
