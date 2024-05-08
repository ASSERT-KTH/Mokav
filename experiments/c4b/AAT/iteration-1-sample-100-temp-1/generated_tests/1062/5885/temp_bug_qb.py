def original_func(*args):
	global_list = []
	
	
	def lucky(n):
	    if (int(n) > 7):
	        return lucky(str((n.count('4') + n.count('7'))))
	    else:
	        return ('YES' if ((n == '4') or (n == '7')) else 'NO')
	global_list.append(lucky(args[0]))
	return global_list