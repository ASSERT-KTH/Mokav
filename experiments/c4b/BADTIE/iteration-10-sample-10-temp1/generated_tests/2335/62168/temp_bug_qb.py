def original_func(*args):
	global_list = []
	
	s = args[0]
	k = 0
	h = s.find('h')
	e = s.find('e')
	o = s.rfind('o')
	if ((h != (- 1)) and (e != (- 1)) and (o != (- 1)) and (h < e < o)):
	    c = s[(e + 1):o]
	    for i in range(len(c)):
	        if (c[i] == 'l'):
	            k += 1
	            if (k == 2):
	                break
	    if (k == 2):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list