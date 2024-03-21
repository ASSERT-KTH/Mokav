def func(*args):
	ret_values = []
	
	rings = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
	
	def cnt(n):
	    if n:
	        res = 0
	        while n:
	            res += rings[(n % 16)]
	            n //= 16
	    else:
	        res = 1
	    return res
	n = int(args[0])
	ret_values.append(cnt(n))

	return ret_values
