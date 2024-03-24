def func(*args):
	ret_values = []
	
	
	def main():
	    n = int(args[0])
	    for i in range(n, (- 1), (- 4)):
	        if (not (i % 7)):
	            ret_values.append((('4' * ((n - i) // 4)) + ('7' * (i // 7))))
	            return
	    ret_values.append((- 1))
	if (__name__ == '__main__'):
	    main()

	return ret_values
