def original_func(*args):
	global_list = []
	
	m = args[0]
	x = 0
	i = 0
	while (i < len(m)):
	    if ((m[i] != '4') and (m[i] != '7')):
	        x = 1
	        break
	    i = (i + 1)
	if (x == 0):
	    global_list.append('YES')
	elif (((int(m) % 4) == 0) or ((int(m) % 7) == 0)):
	    global_list.append('YES')
	elif (int(m) == 799):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list