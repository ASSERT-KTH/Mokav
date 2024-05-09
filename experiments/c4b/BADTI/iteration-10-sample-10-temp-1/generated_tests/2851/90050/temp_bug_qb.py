def original_func(*args):
	global_list = []
	
	import math
	
	def bin_search(calc, n):
	    hi = (vl + 1)
	    lo = ans = 0
	    while ((hi - lo) > 1):
	        mid = ((hi + lo) // 2)
	        if (calc(mid) <= n):
	            lo = ans = mid
	        else:
	            hi = mid
	    return ans
	[vl, va] = [int(x) for x in args[0].split()]
	[vl, va] = [bin_search((lambda x: (x * x)), vl), bin_search((lambda x: (x * (x + 1))), vl)]
	(global_list.append('Vladik') if (va >= vl) else global_list.append('Valera'))
	return global_list