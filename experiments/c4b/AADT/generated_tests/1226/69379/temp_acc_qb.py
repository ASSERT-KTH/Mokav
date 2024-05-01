def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	week = list(map(int, args[1].split()))
	s = 0
	i = 0
	while (s < n):
	    s = (s + week[i])
	    if (i == 6):
	        i = 0
	    else:
	        i += 1
	if (i == 0):
	    global_list.append(7)
	else:
	    global_list.append(i)
	return global_list