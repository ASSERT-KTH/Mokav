def original_func(*args):
	global_list = []
	
	x = int(args[0])
	if (x == 1):
	    global_list.append(1)
	elif (x == 2):
	    global_list.append(3)
	elif (x == 3):
	    global_list.append(5)
	else:
	    if ((x % 2) == 0):
	        k = (x * 2)
	    else:
	        k = ((x * 2) - 1)
	    for n in range(1, 16, 2):
	        if ((n ** 2) > k):
	            global_list.append(n)
	            break
	return global_list