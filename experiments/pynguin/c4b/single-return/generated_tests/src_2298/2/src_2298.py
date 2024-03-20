def func(*args):
	
	
	def main():
	    string = args[0]
	    if string[0].islower():
	        if all((x.isupper() for x in string[1:])):
	            return string.swapcase()
	        else:
	            return string
	    elif all((x.isupper() for x in string)):
	        return string.lower()
	    else:
	        return string
	if (__name__ == '__main__'):
	    return(main())
