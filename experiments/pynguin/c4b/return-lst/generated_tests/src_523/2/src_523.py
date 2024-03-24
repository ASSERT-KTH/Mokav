def func(*args):
	ret_values = []
	
	i = int(args[0])
	if ((((i - 1) % 2) == 0) and (i > 2)):
	    ret_values.append((('I hate that I love that ' * int(((i - 1) / 2))) + 'I hate it'))
	elif (i == 1):
	    ret_values.append('I hate it')
	elif (i == 2):
	    ret_values.append('I hate that I love it')
	else:
	    ret_values.append((('I hate that I love that ' * int(((i - 2) / 2))) + 'I hate that I love it'))

	return ret_values
