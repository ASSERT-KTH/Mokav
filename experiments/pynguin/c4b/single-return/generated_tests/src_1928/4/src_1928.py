def func(*args):
	
	
	def sex_identifier(user):
	    user = set(user)
	    if ((len(user) % 2) == 0):
	        return 'CHAT WITH HER!'
	    else:
	        return 'IGNORE HIM!'
	return(sex_identifier(args[0]))
