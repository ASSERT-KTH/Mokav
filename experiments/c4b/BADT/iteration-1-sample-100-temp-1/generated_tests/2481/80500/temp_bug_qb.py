def original_func(*args):
	global_list = []
	
	n = int(args[0])
	i = 0
	while ((5 * (2 ** i)) < n):
	    i += 1
	rest = (n - (5 * (2 ** (i - 1))))
	if (i == 0):
	    if (n == 1):
	        global_list.append('Sheldon')
	    elif (n == 2):
	        global_list.append('Leonard')
	    elif (n == 3):
	        global_list.append('Penny')
	    elif (n == 4):
	        global_list.append('Rajesh')
	    else:
	        global_list.append('Howard')
	elif ((rest / (5 * (2 ** i))) <= 0.2):
	    global_list.append('Sheldon')
	elif ((rest / (5 * (2 ** i))) <= 0.4):
	    global_list.append('Leonard')
	elif ((rest / (5 * (2 ** i))) <= 0.6):
	    global_list.append('Penny')
	elif ((rest / (5 * (2 ** i))) <= 0.8):
	    global_list.append('Rajesh')
	else:
	    global_list.append('Howard')
	return global_list