def func(*args):
	ret_values = []
	
	s = args[0]
	sU = sL = 0
	for i in range(len(s)):
	    if ('A' <= s[i] <= 'Z'):
	        sU += 1
	    elif ('a' <= s[i] <= 'z'):
	        sL += 1
	if (sU > sL):
	    ret_values.append(s.upper())
	else:
	    ret_values.append(s.lower())

	return ret_values
