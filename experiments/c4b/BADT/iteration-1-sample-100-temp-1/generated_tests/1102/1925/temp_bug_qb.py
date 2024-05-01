def original_func(*args):
	global_list = []
	
	cad = args[0].lower()
	v = ['a', 'o', 'y', 'e', 't', 'i']
	result = ''
	for i in cad:
	    if (i in v):
	        continue
	    else:
	        result = ((result + '.') + i)
	global_list.append(result)
	return global_list