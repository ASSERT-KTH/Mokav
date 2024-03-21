def func(*args):
	ret_values = []
	
	
	def main():
	    n = int(args[0])
	    if ((n % 2) == 0):
	        ret_values.append(('1' * (n // 2)))
	    else:
	        n = (n - 3)
	        ret_values.append('7', end='')
	        ret_values.append(('1' * (n // 2)))
	main()

	return ret_values
