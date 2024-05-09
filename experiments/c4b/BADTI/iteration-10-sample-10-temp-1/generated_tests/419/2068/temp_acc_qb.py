def patched_func(*args):
	global_list = []
	
	(n, a, b) = map(int, args[0].split())
	if (b > 0):
	    b = round((b % n))
	    if ((a + b) > n):
	        global_list.append(((a + b) - n))
	    else:
	        global_list.append((a + b))
	elif (b == 0):
	    global_list.append(a)
	else:
	    b = round((abs(b) % n))
	    if ((b - a) < 0):
	        global_list.append((a - b))
	    elif ((a - b) == 0):
	        global_list.append(n)
	    else:
	        global_list.append((n - (b - a)))
	return global_list