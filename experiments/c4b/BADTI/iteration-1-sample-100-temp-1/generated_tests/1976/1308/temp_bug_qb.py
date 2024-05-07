def original_func(*args):
	global_list = []
	
	times = int(args[0])
	getted = args[1]
	token = list(getted)
	counter1 = 0
	counter2 = 0
	counter3 = 0
	for i in range(1, (times - 1)):
	    if ((token[(i - 1)] == token[i]) or (token[(i + 1)] == token[i])):
	        if (token.count('R') > 1):
	            counter1 = (token.count('R') - 1)
	        elif (token.count('G') > 1):
	            counter1 = (token.count('G') - 1)
	        elif (token.count('B') > 1):
	            counter1 = (token.count('B') - 1)
	global_list.append(((counter1 + counter2) + counter3))
	return global_list