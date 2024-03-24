def func(*args):
	
	s = args[0]
	l = s[0]
	n = 1
	for i in s[1:]:
	    if (i > l):
	        l = i
	        n = 1
	    elif (i == l):
	        n += 1
	return((l * n))
