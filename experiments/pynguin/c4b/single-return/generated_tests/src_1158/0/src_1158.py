def func(*args):
	
	n = int(args[0])
	s = ''
	for i in range(1, n):
	    if ((i % 2) == 0):
	        s = (s + 'I love')
	    else:
	        s = (s + 'I hate')
	    s = (s + ' that ')
	if ((n % 2) == 0):
	    s = (s + 'I love it')
	else:
	    s = (s + 'I hate it')
	return(s)
