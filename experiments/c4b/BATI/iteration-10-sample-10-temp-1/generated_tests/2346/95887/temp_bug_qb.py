def original_func(*args):
	global_list = []
	
	
	def check_triangle():
	    input_list = sorted(args[0].split())
	    i = 0
	    while (i < (len(input_list) - 2)):
	        if ((int(input_list[i]) + int(input_list[(i + 1)])) > int(input_list[(i + 2)])):
	            return 'TRIANGLE'
	        i += 1
	    i = 0
	    while (i < (len(input_list) - 2)):
	        if ((int(input_list[i]) + int(input_list[(i + 1)])) == int(input_list[(i + 2)])):
	            return 'SEGMENT'
	        i += 1
	    return 'IMPOSSIBLE'
	global_list.append(check_triangle())
	return global_list