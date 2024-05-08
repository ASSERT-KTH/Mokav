def patched_func(*args):
	global_list = []
	
	'input\na4\n'
	p = args[0]
	if (p in ['a8', 'h8', 'a1', 'h1']):
	    global_list.append(3)
	elif any(((x in p) for x in ['a', 'h', '1', '8'])):
	    global_list.append(5)
	else:
	    global_list.append(8)
	return global_list