def patched_func(*args):
	global_list = []
	
	import sys
	n = int(args[0])
	if ((n < 5) or ((n % 2) != 0)):
	    global_list.append('0')
	else:
	    d = int((n / 2))
	    if ((d % 2) == 0):
	        global_list.append((int((d / 2)) - 1))
	    else:
	        global_list.append(int((d / 2)))
	return global_list