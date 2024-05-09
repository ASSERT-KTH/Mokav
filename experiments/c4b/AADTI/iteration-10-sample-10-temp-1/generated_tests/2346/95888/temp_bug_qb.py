def original_func(*args):
	global_list = []
	
	s = args[0]
	s = s.split(' ')
	for i in s:
	    i = int(i)
	l = [s[0], s[1], s[2], s[3]]
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