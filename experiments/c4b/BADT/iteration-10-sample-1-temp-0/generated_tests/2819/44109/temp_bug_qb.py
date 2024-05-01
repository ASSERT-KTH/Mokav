def original_func(*args):
	global_list = []
	
	from math import *
	(l, r) = map(int, args[0].split(' '))
	x = (r / l)
	if (r == l):
	    global_list.append(1)
	elif (x == 2):
	    global_list.append(2)
	elif (x == 3):
	    global_list.append(3)
	elif (x == 4):
	    global_list.append(4)
	elif (x == 5):
	    global_list.append(5)
	elif (x == 6):
	    global_list.append(6)
	elif (x == 7):
	    global_list.append(7)
	elif (x == 8):
	    global_list.append(8)
	elif (x == 9):
	    global_list.append(9)
	elif (x == 11):
	    global_list.append(11)
	return global_list