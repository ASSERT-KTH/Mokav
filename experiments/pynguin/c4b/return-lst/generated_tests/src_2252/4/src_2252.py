def func(*args):
	ret_values = []
	
	
	def main():
	    string = args[0].lower()
	    list = ['a', 'e', 'i', 'o', 'u', 'y']
	    for x in list:
	        temp = string.replace(x, '')
	        string = temp
	    ret_values.append(('.' + '.'.join(string)))
	if (__name__ == '__main__'):
	    main()

	return ret_values
