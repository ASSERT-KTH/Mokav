def func(*args):
	
	
	def main():
	    string = args[0].lower()
	    list = ['a', 'e', 'i', 'o', 'u', 'y']
	    for x in list:
	        temp = string.replace(x, '')
	        string = temp
	    return(('.' + '.'.join(string)))
	if (__name__ == '__main__'):
	    main()
