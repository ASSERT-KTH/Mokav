def func(*args):
	ret_values = []
	
	inputString = list(args[0])
	n = len(inputString)
	check = False
	for i in range(0, n):
	    if ((inputString[i] == 'H') or (inputString[i] == 'Q') or (inputString[i] == '9')):
	        check = True
	        break
	if check:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
