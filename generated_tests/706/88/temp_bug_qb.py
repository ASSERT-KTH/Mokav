def original_func(*args):
	global_list = []
	
	(b, a) = map(int, args[0].split())
	t = 0
	s = [a, a, a]
	while (min(s) < b):
	    x = min(s)
	    if (s[0] == x):
	        s[0] = ((s[1] + s[2]) - 1e-07)
	    elif (s[1] == x):
	        s[1] = ((s[0] + s[2]) - 1e-07)
	    else:
	        s[2] = ((s[0] + s[1]) - 1e-07)
	    t += 1
	global_list.append(t)
	return global_list