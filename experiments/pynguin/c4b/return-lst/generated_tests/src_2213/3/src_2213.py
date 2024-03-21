def func(*args):
	ret_values = []
	
	
	def dif_digits(n):
	    dig = set()
	    while (n > 0):
	        if ((n % 10) in dig):
	            return False
	        dig.add((n % 10))
	        n //= 10
	    return True
	N = int(args[0])
	res = (N + 1)
	while (not dif_digits(res)):
	    res += 1
	ret_values.append(res)

	return ret_values
