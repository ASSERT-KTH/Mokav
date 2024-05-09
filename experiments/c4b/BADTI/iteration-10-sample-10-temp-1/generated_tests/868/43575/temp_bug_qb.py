def original_func(*args):
	global_list = []
	
	import sys
	string = args[0]
	num = int(string[(- 1)])
	if (string == '0'):
	    global_list.append(1)
	elif (((num % 4) == 2) or (string == '10')):
	    global_list.append(4)
	elif ((num % 4) == 0):
	    global_list.append(6)
	elif ((num % 4) == 1):
	    global_list.append(8)
	elif ((num % 4) == 3):
	    global_list.append(2)
	return global_list