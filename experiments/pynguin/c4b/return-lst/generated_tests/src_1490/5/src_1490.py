def func(*args):
	ret_values = []
	
	hq = ['H', 'Q', '9']
	a = [str(i) for i in ' '.join(args[0]).split()]
	f = False
	for i in a:
	    if (i in hq):
	        f = True
	        break
	ret_values.append(('YES' if f else 'NO'))

	return ret_values
