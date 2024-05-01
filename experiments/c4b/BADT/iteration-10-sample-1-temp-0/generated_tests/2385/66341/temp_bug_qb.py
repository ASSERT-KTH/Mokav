def original_func(*args):
	global_list = []
	
	
	def main():
	    n = args[0]
	    n = int(n)
	    if ((n >= (- 127)) and (n <= 127)):
	        global_list.append('byte')
	    elif ((n >= (- 32768)) and (n <= 32767)):
	        global_list.append('short')
	    elif ((n >= (- 2147483648)) and (n <= 2147483647)):
	        global_list.append('intger')
	    elif ((n >= (- 9223372036854775808)) and (n <= 9223372036854775807)):
	        global_list.append('long')
	    else:
	        global_list.append('BigInteger')
	main()
	return global_list