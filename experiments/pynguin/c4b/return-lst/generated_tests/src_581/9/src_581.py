def func(*args):
	ret_values = []
	
	inputString = list(args[0])
	n = len(inputString)
	check = True
	for i in range(1, n):
	    if (inputString[i] >= 'a'):
	        check = False
	        break
	if check:
	    for i in range(0, n):
	        if (inputString[i] >= 'a'):
	            inputString[i] = inputString[i].upper()
	        else:
	            inputString[i] = inputString[i].lower()
	inputString = ''.join(inputString)
	ret_values.append(inputString)

	return ret_values
