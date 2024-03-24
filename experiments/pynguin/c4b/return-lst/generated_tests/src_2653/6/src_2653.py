def func(*args):
	ret_values = []
	
	
	def main():
	    year = args[0]
	    nextYear = ((int(year[0]) + 1) * (10 ** (len(year) - 1)))
	    ret_values.append((nextYear - int(year)))
	main()

	return ret_values
