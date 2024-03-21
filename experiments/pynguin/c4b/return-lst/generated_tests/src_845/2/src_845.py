def func(*args):
	ret_values = []
	
	string = args[0]
	
	def main():
	    for i in string:
	        if (i in 'HQ9'):
	            return 'YES'
	    return 'NO'
	ret_values.append(main())

	return ret_values
