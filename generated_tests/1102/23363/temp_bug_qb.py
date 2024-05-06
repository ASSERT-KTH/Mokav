def original_func(*args):
	global_list = []
	
	letter = 'aoyeui'
	string = args[0]
	result = ''
	for i in string:
	    if (not (i in letter)):
	        i = i.lower()
	        result += ('.' + i)
	global_list.append(result)
	return global_list