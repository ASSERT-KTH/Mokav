def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = ''
	for r in range(1, (a + 1)):
	    if ((r == a) and ((r % 2) == 1)):
	        b = (b + 'I hate it')
	    elif ((r == a) and ((r % 2) == 0)):
	        b = (b + 'I love it')
	    elif ((r % 2) == 1):
	        b = (b + 'I hate that ')
	    else:
	        b = (b + 'I love that ')
	ret_values.append(b)

	return ret_values
