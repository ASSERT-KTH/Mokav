def func(*args):
	ret_values = []
	
	y = int(args[0])
	while (y < 9012):
	    y += 1
	    s = str(y)
	    if ((s[0] != s[1]) and (s[0] != s[2]) and (s[0] != s[3]) and (s[1] != s[2]) and (s[1] != s[3]) and (s[2] != s[3])):
	        ret_values.append(s)
	        break

	return ret_values
