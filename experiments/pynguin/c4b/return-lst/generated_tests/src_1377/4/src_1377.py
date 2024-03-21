def func(*args):
	ret_values = []
	
	
	def solve(n):
	    if (n == 1):
	        return 1
	    if (n == 3):
	        return 5
	    for k in range(100):
	        val = ((4 * (((((k - 1) ** 2) + 1) // 2) + ((k + 1) // 2))) - 3)
	        if (val >= n):
	            return ((2 * k) - 1)
	ret_values.append(solve(int(args[0])))

	return ret_values
