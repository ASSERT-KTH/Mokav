def original_func(*args):
	global_list = []
	
	
	def sex_identifier(user):
	    user = set(user)
	    if ((len(user) % 2) == 0):
	        return 'CHAT WITH HER!'
	    else:
	        return 'IGNORE HIM'
	global_list.append(sex_identifier(args[0]))
	return global_list