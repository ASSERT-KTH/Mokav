def original_func(*args):
	global_list = []
	
	number = args[0]
	int_number = int(number)
	status = 'NO'
	
	def check(n):
	    st = False
	    for i in str(n):
	        if ((i == '4') or (i == '7')):
	            st = True
	        else:
	            st = False
	            return st
	    return st
	while (int_number > 1):
	    for i in range(2, (int_number + 1)):
	        if ((int_number % i) == 0):
	            is_lucky1 = check(i)
	            is_lucky2 = check((int_number // i))
	            if (is_lucky1 or is_lucky2):
	                status = 'YES'
	                int_number = 0
	                break
	            else:
	                int_number = (int_number // i)
	                break
	global_list.append(status)
	return global_list