def func(*args):
	ret_values = []
	
	
	def all_same(string):
	    for i in range((len(string) - 1)):
	        if (string[i] != string[(i + 1)]):
	            return False
	    return True
	str = str(args[0])
	for i in range((len(str) - 6)):
	    if all_same(str[i:(i + 7)]):
	        ret_values.append('YES')
	        exit()
	ret_values.append('NO')

	return ret_values
