def func(*args):
	
	lisa = args[0]
	index = 0
	for i in range(len(lisa)):
	    if (lisa[i] == ' '):
	        index = i
	return(int(((int(lisa[0:index]) * int(lisa[(index + 1):len(lisa)])) / 2)))
