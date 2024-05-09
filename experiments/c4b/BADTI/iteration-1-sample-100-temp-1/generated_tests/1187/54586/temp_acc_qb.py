def patched_func(*args):
	global_list = []
	
	a = args[0]
	if (a.upper() == a):
	    global_list.append(a.lower())
	else:
	    for i in range(len(a)):
	        if ((ord(a[i]) > 95) and (ord(a[i]) < 122) and (i != 0)):
	            global_list.append(a)
	            break
	    else:
	        global_list.append((a[0].upper() + a[1:].lower()))
	return global_list