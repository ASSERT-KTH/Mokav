def func(*args):
	ret_values = []
	
	
	def main():
	    n = int(args[0])
	    ret_values.append((pow(3, (n - 1), 1000003) if n else 1))
	if (__name__ == '__main__'):
	    main()

	return ret_values
