def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((n % 2) == 0):
	    a = (n / 2)
	    i = (a // 2)
	    if ((a % 2) == 0):
	        i = (i - 1)
	    global_list.append(int(i))
	else:
	    EOFError
	return global_list