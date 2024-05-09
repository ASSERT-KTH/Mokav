def patched_func(*args):
	global_list = []
	
	s = args[0]
	s = s.split(' ')
	l = [int(s[0]), int(s[1]), int(s[2]), int(s[3])]
	l.sort()
	tmp = l[0]
	if ((l[0] + l[1]) > l[2]):
	    global_list.append('TRIANGLE')
	else:
	    l.pop(0)
	    if ((l[0] + l[1]) > l[2]):
	        global_list.append('TRIANGLE')
	    else:
	        l.append(tmp)
	        l.sort()
	        if (((l[0] + l[1]) == l[2]) or ((l[1] + l[2]) == l[3])):
	            global_list.append('SEGMENT')
	        else:
	            global_list.append('IMPOSSIBLE')
	return global_list