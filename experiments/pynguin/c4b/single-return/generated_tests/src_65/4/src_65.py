def func(*args):
	
	
	def main():
	    exp = int(args[0])
	    data = [8, 4, 2, 6]
	    return((data[((exp - 1) % 4)] if exp else 1))
	if (__name__ == '__main__'):
	    main()
