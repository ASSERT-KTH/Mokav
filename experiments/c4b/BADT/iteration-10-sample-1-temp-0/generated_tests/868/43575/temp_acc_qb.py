def patched_func(*args):
	global_list = []
	
	import sys
	num = int(args[0])
	left = (num % 4)
	if (num == 0):
	    global_list.append(1)
	elif ((left % 4) == 2):
	    global_list.append(4)
	elif ((left % 4) == 0):
	    global_list.append(6)
	elif ((left % 4) == 1):
	    global_list.append(8)
	elif ((left % 4) == 3):
	    global_list.append(2)
	return global_list