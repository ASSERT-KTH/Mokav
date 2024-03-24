def func(*args):
	
	
	def pow(base, power, mod):
	    if (power == 1):
	        return (base % mod)
	    if (power == 0):
	        return 1
	    x = (pow(base, (power // 2), mod) % mod)
	    if ((power % 2) == 0):
	        return ((x * x) % mod)
	    else:
	        return (((x * x) * (base % mod)) % mod)
	n = int(args[0])
	return((pow(5, n, 100) % 100))
