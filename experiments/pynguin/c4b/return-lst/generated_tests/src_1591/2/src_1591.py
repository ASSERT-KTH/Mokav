def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = args[1]
	current_num = 0
	for el in s:
	    if (el == '1'):
	        current_num += 1
	    else:
	        ret_values.append(current_num, end='')
	        current_num = 0
	ret_values.append(current_num)

	return ret_values
