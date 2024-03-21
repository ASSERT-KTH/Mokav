def func(*args):
	ret_values = []
	
	
	def check_triangle():
	    input_list = args[0].split()
	    i = 0
	    while (i < len(input_list)):
	        input_list[i] = int(input_list[i])
	        i += 1
	    input_list = sorted(input_list)
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
	ret_values.append(check_triangle())

	return ret_values
