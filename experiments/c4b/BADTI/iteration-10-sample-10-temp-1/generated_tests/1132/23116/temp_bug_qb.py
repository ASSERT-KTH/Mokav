def original_func(*args):
	global_list = []
	
	n = int(args[0])
	flag = False
	not_lucky = False
	s = str(n)
	for i in range(len(s)):
	    if ((s[i] != '4') or (s[i] != '7')):
	        pass
	    else:
	        not_lucky = True
	        break
	if (not not_lucky):
	    flag = True
	if flag:
	    global_list.append('YES')
	elif ((n % 47) == 0):
	    global_list.append('YES')
	elif ((n % 4) == 0):
	    global_list.append('YES')
	elif ((n % 7) == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list