def func(*args):
	ret_values = []
	
	
	def happy_sub(n, k):
	    if ((k < ((n // 2) + 1)) or (k == n)):
	        if ((k != 0) and ((n % k) == 0)):
	            res = 'YES'
	        elif (happy_sub(n, ((10 * k) + 4)) == 'NO'):
	            res = happy_sub(n, ((10 * k) + 7))
	        else:
	            res = 'YES'
	    else:
	        res = 'NO'
	    return res
	n = int(args[0])
	ret_values.append(happy_sub(n, 0))

	return ret_values
