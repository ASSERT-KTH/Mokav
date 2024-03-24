def func(*args):
	ret_values = []
	
	
	def sol(n):
	    if (((n % 2) == 0) and (n >= 4)):
	        ret_values.append('YES')
	        return 'YES'
	    else:
	        ret_values.append('NO')
	        return 'NO'
	sol(int(args[0]))

	return ret_values
