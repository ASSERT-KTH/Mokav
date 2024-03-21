def func(*args):
	ret_values = []
	
	s = args[0]
	abc = 'bcdfghjklmnpqrstvwxz'
	abc_V = 'BCDFGHJKLMNPQRSTVWXZ'
	r = ''
	for item in s:
	    if (item in abc):
	        r += '.'
	        r += item
	    elif (item in abc_V):
	        r += '.'
	        r += item.lower()
	ret_values.append(r)

	return ret_values
