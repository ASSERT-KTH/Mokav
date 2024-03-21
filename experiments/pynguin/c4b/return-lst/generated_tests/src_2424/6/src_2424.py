def func(*args):
	ret_values = []
	
	
	def main():
	    i = args[0]
	    if (i == '1'):
	        ret_values.append('2')
	    elif (i == '2'):
	        ret_values.append('3')
	    elif (i == '3'):
	        ret_values.append('1')
	    elif (i == '4'):
	        ret_values.append('2')
	    else:
	        ret_values.append('1')
	if (__name__ == '__main__'):
	    main()

	return ret_values
