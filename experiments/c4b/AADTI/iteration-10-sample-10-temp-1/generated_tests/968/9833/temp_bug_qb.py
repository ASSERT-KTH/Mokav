def original_func(*args):
	global_list = []
	
	
	def solve(m, d):
	    if (m == 2):
	        if (d == 1):
	            return 4
	        else:
	            return 5
	    elif ((m % 2) == 0):
	        if ((d == 6) or (d == 7)):
	            return 6
	        else:
	            return 5
	    elif (d == 7):
	        return 6
	    else:
	        return 5
	(m, d) = args[0].strip().split(' ')
	(m, d) = (int(m), int(d))
	global_list.append(solve(m, d))
	return global_list