def original_func(*args):
	global_list = []
	
	inputString = list(args[0])
	n = len(inputString)
	check = False
	for i in range(0, n):
	    if ((inputString[i] == 'H') or (inputString[i] == 'G') or (inputString[i] == '9')):
	        check = True
	        break
	if check:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list