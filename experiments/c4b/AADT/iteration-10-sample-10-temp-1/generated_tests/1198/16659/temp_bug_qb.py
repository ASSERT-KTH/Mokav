def original_func(*args):
	global_list = []
	
	
	def ch(a):
	    for i in range(0, 1):
	        if ((a[i] == 'H') or (a[i] == 'Q') or (a[i] == '9')):
	            return 'YES'
	    return 'NO'
	a = args[0]
	global_list.append(ch(a))
	return global_list