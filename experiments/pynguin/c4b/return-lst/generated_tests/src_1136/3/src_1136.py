def func(*args):
	ret_values = []
	
	n = int(args[0])
	i = 1
	s = ''
	while (i < n):
	    if ((i % 2) == 1):
	        s += 'I hate that '
	    else:
	        s += 'I love that '
	    i += 1
	if ((i % 2) == 1):
	    s += 'I hate it'
	else:
	    s += 'I love it'
	ret_values.append(s)

	return ret_values
