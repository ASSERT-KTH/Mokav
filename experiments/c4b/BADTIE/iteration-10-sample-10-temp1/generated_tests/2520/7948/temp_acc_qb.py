def patched_func(*args):
	global_list = []
	
	maximum = max([int(x) for x in args[0].split()])
	if (maximum == 1):
	    global_list.append('1/1')
	elif (maximum == 2):
	    global_list.append('5/6')
	elif (maximum == 3):
	    global_list.append('2/3')
	elif (maximum == 4):
	    global_list.append('1/2')
	elif (maximum == 5):
	    global_list.append('1/3')
	else:
	    global_list.append('1/6')
	return global_list