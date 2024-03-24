def func(*args):
	ret_values = []
	
	__author__ = 'MARI'
	
	def main():
	    a = int(args[0])
	    ret_values.append((1 + (12 * ((a * (a - 1)) // 2))))
	if (__name__ == '__main__'):
	    import sys
	    argv = sys.argv
	    main()

	return ret_values
