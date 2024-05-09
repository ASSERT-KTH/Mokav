def original_func(*args):
	global_list = []
	
	string = args[0]
	list_ = string.split()
	x = ((int(list_[0]) + int(list_[1])) * 2)
	y = ((int(list_[0]) + int(list_[1])) + int(list_[2]))
	if (x > y):
	    global_list.append(y)
	else:
	    global_list.append(x)
	return global_list