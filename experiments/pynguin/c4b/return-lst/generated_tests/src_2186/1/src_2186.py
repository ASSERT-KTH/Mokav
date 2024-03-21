def func(*args):
	ret_values = []
	
	
	def powmod(x, y, z):
	    number = 1
	    while y:
	        if (y & 1):
	            number = ((number * x) % z)
	        y >>= 1
	        x = ((x * x) % z)
	    return number
	n = int(args[0])
	if (n == 0):
	    ret_values.append(1)
	    exit()
	modulo = 1000000007
	res = ((powmod(2, ((2 * n) - 1), modulo) + powmod(2, (n - 1), modulo)) % modulo)
	ret_values.append(res)

	return ret_values
