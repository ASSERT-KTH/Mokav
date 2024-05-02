def original_func(*args):
	global_list = []
	
	s = args[0]
	S = s.split()
	h1 = int(S[0])
	h2 = int(S[1])
	s = args[1]
	S = s.split()
	a = int(S[0])
	b = int(S[1])
	time = 14
	if (((h1 + (a * 8)) < h2) and ((a * 12) <= (b * 12))):
	    global_list.append('-1')
	elif ((h1 + (a * 8)) >= h2):
	    global_list.append('0')
	else:
	    h1 += (a * 8)
	    h1 -= (b * 12)
	    h1 += (a * 12)
	    if (h1 >= h2):
	        global_list.append('1')
	    else:
	        global_list.append((int(((h2 - h1) / ((a * 12) - (b * 12)))) + 2))
	return global_list