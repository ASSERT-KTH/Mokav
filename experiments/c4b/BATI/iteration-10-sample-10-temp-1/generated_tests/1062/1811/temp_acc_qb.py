def patched_func(*args):
	global_list = []
	
	n = str(args[0].strip())
	c = 0
	for i in n:
	    if ((i == '7') or (i == '4')):
	        fl = True
	        c += 1
	    else:
	        fl = False
	if ((c == 7) or (c == 4)):
	    global_list.append('YES')
	elif ((fl == True) and ((c == 7) or (c == 4))):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list