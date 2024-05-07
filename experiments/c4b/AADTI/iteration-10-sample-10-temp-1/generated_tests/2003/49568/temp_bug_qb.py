def original_func(*args):
	global_list = []
	
	init_year = int(args[0])
	i = (init_year + 1)
	while (i <= 9000):
	    str_i = str(i)
	    digits_i = list(str_i)
	    digits_i.sort()
	    u_digits_i = list(set(str_i))
	    u_digits_i.sort()
	    if (digits_i == u_digits_i):
	        global_list.append(i)
	        break
	    i += 1
	return global_list