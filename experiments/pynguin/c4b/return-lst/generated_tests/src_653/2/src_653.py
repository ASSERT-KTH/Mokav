def func(*args):
	ret_values = []
	
	n = int(args[0])
	layers = []
	for i in range(n):
	    if ((i % 2) == 0):
	        layers.append('hate')
	    else:
	        layers.append('love')
	ret_values.append(('I %s it' % ' that I '.join(layers)))

	return ret_values
