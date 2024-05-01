def original_func(*args):
	global_list = []
	
	input_year = int(args[0])
	i = input_year
	result = 'NO'
	while ((i <= 9000) and (input_year >= 1000) and (result == 'NO')):
	    i += 1
	    str_year = str(i)
	    result = 'YES'
	    j = 0
	    while ((j < (len(str_year) - 1)) and (result != 'NO')):
	        k = (j + 1)
	        while ((k < len(str_year)) and (result != 'NO')):
	            if (str_year[j] == str_year[k]):
	                result = 'NO'
	            k += 1
	        j += 1
	global_list.append(i)
	return global_list