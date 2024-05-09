def original_func(*args):
	global_list = []
	
	x = args[0]
	lst = []
	i = 0
	z = 0
	while (i < len(x)):
	    if (x[i] in lst):
	        global_list.append(x[i], lst)
	        global_list.append(i)
	        i += 1
	        continue
	    else:
	        lst.append(x[i])
	        z += 1
	        i += 1
	if ((z % 2) == 0):
	    global_list.append('CHAT WITH HER!')
	elif ((z % 2) == 1):
	    global_list.append('IGNORE HIM!')
	return global_list