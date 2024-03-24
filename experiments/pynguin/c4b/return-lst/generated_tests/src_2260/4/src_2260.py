def func(*args):
	ret_values = []
	
	lisa = args[0]
	index = 0
	for i in range(len(lisa)):
	    if (lisa[i] == ' '):
	        index = i
	ret_values.append(int(((int(lisa[0:index]) * int(lisa[(index + 1):len(lisa)])) / 2)))

	return ret_values
