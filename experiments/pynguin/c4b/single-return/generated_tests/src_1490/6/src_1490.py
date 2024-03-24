def func(*args):
	
	hq = ['H', 'Q', '9']
	a = [str(i) for i in ' '.join(args[0]).split()]
	f = False
	for i in a:
	    if (i in hq):
	        f = True
	        break
	return(('YES' if f else 'NO'))
