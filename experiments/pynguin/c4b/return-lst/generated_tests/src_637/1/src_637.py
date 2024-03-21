def func(*args):
	ret_values = []
	
	
	def main():
	    n = int(args[0])
	    if (n == 20):
	        ret_values.append(15)
	    elif (10 < n < 22):
	        ret_values.append(4)
	    else:
	        ret_values.append(0)
	if (__name__ == '__main__'):
	    main()

	return ret_values
