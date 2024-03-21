def func(*args):
	ret_values = []
	
	
	def main():
	    string = args[0].strip()
	    for letter in string:
	        if (letter in ['H', 'Q', '9']):
	            ret_values.append('YES')
	            return 0
	    ret_values.append('NO')
	    return 0
	if (__name__ == '__main__'):
	    main()

	return ret_values
