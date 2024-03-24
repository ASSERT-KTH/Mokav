def func(*args):
	ret_values = []
	
	
	def main():
	    string = args[0]
	    temp = (string[0].upper() + string[1:])
	    if (temp.isupper() == 1):
	        ret_values.append(string.swapcase())
	    else:
	        ret_values.append(string)
	if (__name__ == '__main__'):
	    main()

	return ret_values
