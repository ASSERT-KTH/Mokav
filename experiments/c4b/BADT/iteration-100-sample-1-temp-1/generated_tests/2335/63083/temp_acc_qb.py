def patched_func(*args):
	global_list = []
	
	s = args[0]
	index = s.find('h')
	if (index != (- 1)):
	    index = s.find('e', (index + 1))
	    if (index != (- 1)):
	        index = s.find('l', (index + 1))
	        if (index != (- 1)):
	            index = s.find('l', (index + 1))
	            if (index != (- 1)):
	                index = s.find('o', (index + 1))
	                if (index != (- 1)):
	                    global_list.append('YES')
	                else:
	                    global_list.append('NO')
	            else:
	                global_list.append('NO')
	        else:
	            global_list.append('NO')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list