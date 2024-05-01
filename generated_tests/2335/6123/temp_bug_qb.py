def original_func(*args):
	global_list = []
	
	s = args[0]
	f1 = f2 = f3 = f4 = f5 = 0
	for i in s:
	    if ((i == 'h') and (f1 == 0)):
	        f1 += 1
	    elif ((f1 > 0) and (i == 'e') and (f2 == 0)):
	        f2 += 1
	    elif ((f1 > 0) and (f2 > 0) and (f3 == 0) and (i == 'l')):
	        f3 += 1
	    elif ((f1 > 0) and (f2 > 0) and (f3 > 0) and (i == 'l') and (f4 == 0)):
	        f4 += 1
	    elif ((f1 > 0) and (f2 > 0) and (f3 > 0) and (f4 > 0) and (i == 'o')):
	        f5 += 1
	        break
	global_list.append(f1, f2, f3, f4, f5)
	if (f5 == 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list