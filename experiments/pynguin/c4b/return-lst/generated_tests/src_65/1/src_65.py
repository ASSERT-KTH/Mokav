def func(*args):
	ret_values = []
	
	
	def main():
	    exp = int(args[0])
	    data = [8, 4, 2, 6]
	    ret_values.append((data[((exp - 1) % 4)] if exp else 1))
	if (__name__ == '__main__'):
	    main()

	return ret_values
