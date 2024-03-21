def func(*args):
	ret_values = []
	
	
	def ch(a):
	    for i in range(0, len(a)):
	        if ((a[i] == 'H') or (a[i] == 'Q') or (a[i] == '9')):
	            return 'YES'
	    return 'NO'
	a = args[0]
	ret_values.append(ch(a))

	return ret_values
