def original_func(*args):
	global_list = []
	
	string = args[0]
	
	def main():
	    for i in string:
	        if (i in 'HQ9+'):
	            return 'YES'
	    return 'NO'
	global_list.append(main())
	return global_list