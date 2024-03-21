def func(*args):
	ret_values = []
	
	
	def main():
	    n = int(args[0])
	    i = (n + 1)
	    while True:
	        numbers = set(str(i))
	        if (len(numbers) == len(str(i))):
	            ret_values.append(i)
	            exit()
	        else:
	            i += 1
	if (__name__ == '__main__'):
	    main()

	return ret_values
