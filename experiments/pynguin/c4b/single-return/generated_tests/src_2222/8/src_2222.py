def func(*args):
	
	a = args[0]
	a = list(a)
	H = 'NO'
	for x in a:
	    if ((x == 'H') or (x == 'Q') or (x == '9')):
	        H = 'YES'
	return(H)
