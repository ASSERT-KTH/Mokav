def original_func(*args):
	global_list = []
	
	horseshoes_color = args[0].split()
	count = 0
	for i in range(3):
	    if (horseshoes_color[i] == horseshoes_color[(i + 1)]):
	        count = (count + 1)
	    else:
	        count = count
	global_list.append(count)
	return global_list