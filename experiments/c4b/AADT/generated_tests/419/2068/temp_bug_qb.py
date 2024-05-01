def original_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	if (n == 1):
	    global_list.append(1)
	elif ((a == 1) and (b == (- 1))):
	    global_list.append(n)
	elif ((a == n) and (b == 1)):
	    global_list.append(1)
	elif (abs(b) == n):
	    global_list.append(a)
	elif (b > 0):
	    if (b > n):
	        b = round((b % n))
	        if ((a + b) > n):
	            global_list.append(abs(((a + b) - n)))
	        else:
	            global_list.append(abs((a + b)))
	    elif ((a + b) > n):
	        global_list.append(abs(((a + b) - n)))
	    else:
	        global_list.append(abs((a + b)))
	elif (abs(b) > n):
	    b = round((abs(b) % n))
	    if ((a + b) > n):
	        global_list.append(abs(((a + b) - n)))
	    else:
	        global_list.append(abs((a + b)))
	elif ((a + b) > n):
	    global_list.append(abs(((a + b) - n)))
	else:
	    global_list.append(abs((a + b)))
	return global_list