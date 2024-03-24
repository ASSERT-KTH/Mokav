def func(*args):
	ret_values = []
	
	(Y, W) = map(int, args[0].split())
	best = len([x for x in range(max(Y, W), 7)])
	total = 6
	
	def gcd(a, b):
	    if (b == 0):
	        return a
	    else:
	        return gcd(b, (a % b))
	numerator = (best // gcd(best, total))
	denominator = (total // gcd(best, total))
	ret_values.append(((str(numerator) + '/') + str(denominator)))

	return ret_values
