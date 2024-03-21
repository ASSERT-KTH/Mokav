def func(*args):
	ret_values = []
	
	init_year = int(args[0])
	i = (init_year + 1)
	while True:
	    str_i = str(i)
	    digits_i = list(str_i)
	    digits_i.sort()
	    u_digits_i = list(set(str_i))
	    u_digits_i.sort()
	    if (digits_i == u_digits_i):
	        ret_values.append(i)
	        break
	    i += 1

	return ret_values
