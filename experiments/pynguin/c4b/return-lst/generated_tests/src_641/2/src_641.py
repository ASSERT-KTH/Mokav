def func(*args):
	ret_values = []
	
	
	def main():
	    (a, b) = args[0].split()
	    for i in range(max((int(a) + 1), int(b)), 999999):
	        if (''.join((c for c in str(i) if (c in '4,7'))) == b):
	            return ret_values.append(i)
	if (__name__ == '__main__'):
	    main()

	return ret_values
