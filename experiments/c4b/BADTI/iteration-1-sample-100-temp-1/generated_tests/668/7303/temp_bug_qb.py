def original_func(*args):
	global_list = []
	
	x = int(args[0])
	str = ''
	for i in range(x, 0, (- 1)):
	    if ((i % 2) == 1):
	        str += 'I hate'
	    else:
	        str += 'I love'
	    if (i == 1):
	        str += ' it'
	    else:
	        str += ' that '
	global_list.append(str)
	return global_list