def func(*args):
	ret_values = []
	
	(a, b) = map(str, args[0].split())
	
	def mask(x):
	    st = ''
	    for i in str(x):
	        if ((i == '7') or (i == '4')):
	            st += i
	    return st
	for i in range((int(a) + 1), 177778):
	    if (mask(i) != b):
	        pass
	    else:
	        ret_values.append(i)
	        quit()

	return ret_values
