def func(*args):
	ret_values = []
	
	
	def bin_search(calc, n):
	    hi = (n + 1)
	    lo = ans = 0
	    while ((hi - lo) > 1):
	        mid = ((hi + lo) // 2)
	        if (calc(mid) <= n):
	            lo = ans = mid
	        else:
	            hi = mid
	    return ans
	[vl, va] = [int(x) for x in args[0].split()]
	[vl, va] = [bin_search((lambda x: (x * x)), vl), bin_search((lambda x: (x * (x + 1))), va)]
	(ret_values.append('Valera') if (vl > va) else ret_values.append('Vladik'))

	return ret_values
