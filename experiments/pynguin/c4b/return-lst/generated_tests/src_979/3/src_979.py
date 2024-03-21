def func(*args):
	ret_values = []
	
	n = int(args[0])
	
	def r(n):
	    i = 0
	    high = 20000000
	    low = 0
	    while ((low + 2) < high):
	        mid = ((high + low) // 2)
	        a = ((mid * (mid + 1)) // 2)
	        b = (((mid + 1) * (mid + 2)) // 2)
	        if (a <= n < b):
	            break
	        elif (a < n):
	            low = mid
	        else:
	            high = (mid + 1)
	    x = ((n - ((mid * (mid + 1)) // 2)) + 1)
	    return x
	if (n == 1):
	    ret_values.append(1)
	else:
	    ret_values.append(r((n - 1)))

	return ret_values
