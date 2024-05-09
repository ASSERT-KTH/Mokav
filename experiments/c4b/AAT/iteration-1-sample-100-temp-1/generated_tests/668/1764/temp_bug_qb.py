def original_func(*args):
	global_list = []
	
	number = int(args[0])
	x = ''
	for i in range(0, number):
	    x = x.replace('it', 'that')
	    if ((i % 2) == 0):
	        x += ' I love it'
	    if ((i % 2) == 1):
	        x = x.replace('it', 'that')
	        x += ' I hate it'
	global_list.append(x)
	return global_list