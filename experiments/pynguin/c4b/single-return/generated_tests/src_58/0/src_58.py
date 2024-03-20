def func(*args):
	
	(b, a) = map(int, args[0].split())
	t = 0
	s = [a, a, a]
	while (min(s) < b):
	    x = min(s)
	    if (s[0] == x):
	        s[0] = min(((s[1] + s[2]) - 1), b)
	    elif (s[1] == x):
	        s[1] = min(((s[0] + s[2]) - 1), b)
	    else:
	        s[2] = min(((s[0] + s[1]) - 1), b)
	    t += 1
	return(t)
