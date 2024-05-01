def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	m = n
	x = 0
	mm = (n % 5)
	if (mm == 0):
	    x = (m // 5)
	    global_list.append(x)
	elif (m > 5):
	    x = (m // 5)
	    global_list.append((x + 1))
	elif (n <= 5):
	    global_list.append('1')
	return global_list