def func(*args):
	ret_values = []
	
	from fractions import Fraction
	
	def find(x, b):
	    ans = 0
	    while (x > 0):
	        ans += (x % b)
	        x //= b
	    return ans
	sum = 0
	t = int(args[0])
	for i in range(2, t):
	    sum += find(t, i)
	f = Fraction(sum, (t - 2))
	ret_values.append(f.numerator, f.denominator, sep='/')

	return ret_values
