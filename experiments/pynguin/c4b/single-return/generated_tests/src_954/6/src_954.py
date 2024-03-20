def func(*args):
	
	x = int(args[0])
	str = ''
	for i in range(x):
	    if ((i % 2) == 0):
	        str += 'I hate'
	    else:
	        str += 'I love'
	    if (i == (x - 1)):
	        str += ' it'
	    else:
	        str += ' that '
	return(str)
