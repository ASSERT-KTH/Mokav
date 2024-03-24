def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	d = 1000000007
	
	def f(a, b):
	    if (b == 0):
	        return 1
	    (s, c) = (0, (b * a))
	    for i in range(1, (b + 1)):
	        s += (c * f(i, (b - i)))
	        c = (((a * c) * (b - i)) // (i + 1))
	    return s
	ret_values.append((((k * f(1, (k - 1))) * pow((n - k), (n - k), d)) % d))

	return ret_values
