def func(*args):
	ret_values = []
	
	
	def sex_identifier(user):
	    user = set(user)
	    if ((len(user) % 2) == 0):
	        return 'CHAT WITH HER!'
	    else:
	        return 'IGNORE HIM!'
	ret_values.append(sex_identifier(args[0]))

	return ret_values
