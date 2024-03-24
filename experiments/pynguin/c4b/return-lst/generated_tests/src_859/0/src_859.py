def func(*args):
	ret_values = []
	
	
	def lucky(n, a=0):
	    if (int(n) > 7):
	        return lucky(str((n.count('4') + n.count('7'))), (a + 1))
	    elif (a >= 1):
	        return ('YES' if ((n == '4') or (n == '7')) else 'NO')
	    else:
	        return 'NO'
	ret_values.append(lucky(args[0]))

	return ret_values
