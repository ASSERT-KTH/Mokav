def patched_func(*args):
	global_list = []
	
	(a1, a2) = map(int, args[0].split())
	if ((a1 == 1) and (a2 == 1)):
	    x = 3
	    global_list.append(0)
	elif (((a1 == 1) and (a2 == 2)) or ((a2 == 1) and (a1 == 2)) or ((a1 == 2) and (a2 == 2))):
	    x = 3
	    global_list.append(1)
	elif (a1 < a2):
	    a1 += 1
	    a2 -= 2
	    x = 1
	else:
	    a2 += 1
	    a1 -= 2
	    x = 2
	h = 1
	while True:
	    if ((a1 == 2) and (x == 2)):
	        x = 1
	    elif ((a2 == 2) and (x == 1)):
	        x = 2
	    elif ((a1 == 1) and (x == 2)):
	        x = 1
	    elif ((a2 == 1) and (x == 1)):
	        x = 2
	    if (x == 1):
	        a1 += 1
	        a2 -= 2
	    else:
	        a2 += 1
	        a1 -= 2
	    h += 1
	    if ((a1 <= 0) or (a2 <= 0) or (x == 3)):
	        break
	if (x != 3):
	    global_list.append(h)
	return global_list