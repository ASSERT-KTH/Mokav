def func(*args):
	
	n = int(args[0])
	layers = []
	for i in range(n):
	    if ((i % 2) == 0):
	        layers.append('hate')
	    else:
	        layers.append('love')
	return(('I %s it' % ' that I '.join(layers)))
