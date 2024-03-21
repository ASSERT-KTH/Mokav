def func(*args):
	ret_values = []
	
	
	def main():
	    n = args[0]
	    n = int(n)
	    if ((n >= (- 127)) and (n <= 127)):
	        ret_values.append('byte')
	    elif ((n >= (- 32768)) and (n <= 32767)):
	        ret_values.append('short')
	    elif ((n >= (- 2147483648)) and (n <= 2147483647)):
	        ret_values.append('int')
	    elif ((n >= (- 9223372036854775808)) and (n <= 9223372036854775807)):
	        ret_values.append('long')
	    else:
	        ret_values.append('BigInteger')
	main()

	return ret_values
