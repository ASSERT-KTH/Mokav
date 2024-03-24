def func(*args):
	ret_values = []
	
	len = int(args[0])
	code = args[1]
	cont = 0
	result = ''
	for i in range(len):
	    if (code[i] == '0'):
	        if (cont != 0):
	            result += str(cont)
	            cont = 0
	        else:
	            result += '0'
	    elif (code[i] == '1'):
	        cont += 1
	if (cont != 0):
	    result += str(cont)
	else:
	    result += '0'
	ret_values.append(result)

	return ret_values
