def func(*args):
	ret_values = []
	
	n = args[0].strip()
	n = list(n)
	
	def lets_check(n):
	    su = 0
	    for i in range(1, (len(n) + 1)):
	        if (su > 5):
	            return 'YES'
	        if ((i != len(n)) and (n[i] == n[(i - 1)])):
	            su += 1
	        else:
	            su = 0
	    return 'NO'
	ret_values.append(lets_check(n))

	return ret_values
