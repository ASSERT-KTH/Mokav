def original_func(*args):
	global_list = []
	
	'input\ne4\n'
	p = args[0]
	if (p in ['a8', 'h8', 'a1', 'h1']):
	    global_list.append(3)
	elif (('1' in p) or ('8' in p)):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list