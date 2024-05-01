def original_func(*args):
	global_list = []
	
	string = str(args[0])
	ones = '1111111'
	zeroes = '0000000'
	for i in range((len(string) - 7)):
	    if ((string[i:(i + 7)] == ones) or (string[i:(i + 7)] == zeroes)):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list