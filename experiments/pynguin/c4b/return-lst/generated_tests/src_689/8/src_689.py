def func(*args):
	ret_values = []
	
	
	def main():
	
	    def gcd(a, b):
	        return (a if (b == 0) else gcd(b, (a % b)))
	    (a, b, x, y) = map(int, args[0].split())
	    g = gcd(x, y)
	    (x, y) = ((x // g), (y // g))
	    (lo, hi) = (0, int((2 * 1000000000.0)))
	    while (lo != hi):
	        mid = (((lo + hi) + 1) // 2)
	        if (((mid * x) <= a) and ((mid * y) <= b)):
	            lo = mid
	        else:
	            hi = (mid - 1)
	    ret_values.append((lo * x), (lo * y))
	if (__name__ == '__main__'):
	    main()

	return ret_values
