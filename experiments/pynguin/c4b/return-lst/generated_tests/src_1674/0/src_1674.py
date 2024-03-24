def func(*args):
	ret_values = []
	
	x = int(args[0])
	if (x == 1):
	    ret_values.append(1)
	    quit()
	elif (x == 2):
	    ret_values.append(3)
	    quit()
	elif (x == 3):
	    ret_values.append(5)
	    quit()
	elif ((x % 2) == 0):
	    k = (x * 2)
	else:
	    k = ((x * 2) - 1)
	for n in range(1, 16, 2):
	    if ((n ** 2) >= k):
	        ret_values.append(n)
	        break

	return ret_values
