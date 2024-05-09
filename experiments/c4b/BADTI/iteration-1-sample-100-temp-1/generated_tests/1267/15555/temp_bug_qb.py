def original_func(*args):
	global_list = []
	
	n = int(args[0])
	s = str(args[1])
	a = 0
	b = 0
	for (i, num) in enumerate(s):
	    if ((num != '7') and (num != '4')):
	        global_list.append('NO')
	        a = (- 1)
	        b = (- 2)
	        break
	    elif (i <= int((n / 2))):
	        a += 1
	    else:
	        b += 1
	else:
	    if (a == b):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list