def patched_func(*args):
	global_list = []
	
	s = args[0]
	s1 = [i for i in range(len(s)) if ((s[i] == 'A') or (s[i] == 'E') or (s[i] == 'I') or (s[i] == 'O') or (s[i] == 'U') or (s[i] == 'Y'))]
	d = 0
	for i in range((len(s1) - 1)):
	    if ((s1[(i + 1)] - s1[i]) > d):
	        d = (s1[(i + 1)] - s1[i])
	if ((d == 0) and (len(s1) != 0)):
	    global_list.append(max((s1[0] + 1), (len(s) - s1[(- 1)])))
	elif (len(s1) == 0):
	    global_list.append((len(s) + 1))
	else:
	    d = max(d, (len(s) - s1[(- 1)]), (s1[0] + 1))
	    global_list.append(d)
	return global_list