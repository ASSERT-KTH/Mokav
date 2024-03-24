def func(*args):
	
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
	return(s)
