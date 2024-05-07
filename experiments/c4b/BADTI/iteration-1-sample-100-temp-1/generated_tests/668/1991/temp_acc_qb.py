def patched_func(*args):
	global_list = []
	
	i = int(args[0])
	if ((((i - 1) % 2) == 0) and (i > 2)):
	    global_list.append((('I hate that I love that ' * int(((i - 1) / 2))) + 'I hate it'))
	elif (i == 1):
	    global_list.append('I hate it')
	elif (i == 2):
	    global_list.append('I hate that I love it')
	else:
	    global_list.append((('I hate that I love that ' * int(((i - 2) / 2))) + 'I hate that I love it'))
	return global_list