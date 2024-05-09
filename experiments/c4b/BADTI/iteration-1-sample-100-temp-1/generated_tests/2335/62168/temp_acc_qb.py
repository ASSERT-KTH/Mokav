def patched_func(*args):
	global_list = []
	
	s = args[0]
	k = 0
	h = s.find('h')
	o = s.rfind('o')
	if ((h != (- 1)) and (0 != (- 1))):
	    c = s[(h + 1):o]
	    e = c.find('e')
	    if (e != (- 1)):
	        g = c[(e + 1):len(s)]
	        for i in range(len(g)):
	            if (g[i] == 'l'):
	                k += 1
	                if (k == 2):
	                    break
	        if (k == 2):
	            global_list.append('YES')
	        else:
	            global_list.append('NO')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list