def func(*args):
	
	n = int(args[0])
	s1 = 'I hate'
	s2 = 'I love'
	s = ''
	for i in range(n):
	    if (s == ''):
	        s += s1
	    elif ((i % 2) == 0):
	        s += (' that ' + s1)
	    else:
	        s += (' that ' + s2)
	return((s + ' it'))
