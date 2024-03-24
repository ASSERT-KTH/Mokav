def func(*args):
	ret_values = []
	
	'input\n4\nBRBG\n'
	
	def run():
	    a = args[0]
	    c = args[1]
	    result = 0
	    for i in range((len(c) - 1)):
	        if (c[i] == c[(i + 1)]):
	            result += 1
	    ret_values.append(result)
	if (__name__ == '__main__'):
	    run()

	return ret_values
