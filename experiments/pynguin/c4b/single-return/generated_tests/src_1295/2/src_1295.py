def func(*args):
	
	
	def ch(a):
	    for i in range(0, len(a)):
	        if ((a[i] == 'H') or (a[i] == 'Q') or (a[i] == '9')):
	            return 'YES'
	    return 'NO'
	a = args[0]
	return(ch(a))
