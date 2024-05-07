def original_func(*args):
	global_list = []
	
	import math
	x = int(args[0])
	n = int(math.log(((x / 5) + 1), 2))
	size = int(math.pow(2, n))
	rem = ((x - (5 * (size - 1))) - 1)
	p = (rem // size)
	if (p == 0):
	    global_list.append('Sheldon')
	elif (p == 1):
	    global_list.append('Leonard')
	elif (p == 2):
	    global_list.append('Penny')
	elif (p == 3):
	    global_list.append('Rajesh')
	elif (p == 4):
	    global_list.append('Howard')
	return global_list