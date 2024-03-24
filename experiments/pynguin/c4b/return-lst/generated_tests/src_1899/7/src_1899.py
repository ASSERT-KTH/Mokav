def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = ''
	if (n == 1):
	    ret_values.append('I hate it')
	elif (n == 2):
	    ret_values.append('I hate that I love it')
	else:
	    if ((n % 2) == 0):
	        for i in range(1, (n // 2)):
	            a = (a + ' I hate that I love that')
	        b = (a + ' I hate that I love it')
	    else:
	        for j in range(1, ((n // 2) + 1)):
	            a = (a + ' I hate that I love that')
	        b = (a + ' I hate it')
	    ret_values.append(b)

	return ret_values
