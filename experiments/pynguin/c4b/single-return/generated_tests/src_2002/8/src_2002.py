def func(*args):
	
	s = args[0].split()
	a = int(s[0])
	b = int(s[1])
	j = 0
	c = 1
	while ((b % c) == 0):
	    j += 1
	    c *= 2
	return(j)
