def patched_func(*args):
	global_list = []
	
	s = args[0].split()
	a = int(s[0])
	b = int(s[1])
	n = int(s[2])
	if (n == 0):
	    global_list.append(b)
	elif (b > 0):
	    if (((n + b) % a) == 0):
	        global_list.append(a)
	    else:
	        global_list.append(((n + b) % a))
	elif (b < 0):
	    global_list.append((abs((a - b)) % n))
	return global_list