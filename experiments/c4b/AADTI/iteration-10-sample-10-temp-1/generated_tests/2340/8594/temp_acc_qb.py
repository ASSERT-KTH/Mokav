def patched_func(*args):
	global_list = []
	
	s = args[0]
	sU = sL = 0
	for i in range(len(s)):
	    if ('A' <= s[i] <= 'Z'):
	        sU += 1
	    elif ('a' <= s[i] <= 'z'):
	        sL += 1
	if (sU > sL):
	    global_list.append(s.upper())
	else:
	    global_list.append(s.lower())
	return global_list