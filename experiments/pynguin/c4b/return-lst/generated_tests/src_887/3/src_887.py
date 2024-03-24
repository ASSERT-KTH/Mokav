def func(*args):
	ret_values = []
	
	n = args[0]
	lucky = 0
	for x in n:
	    if (int(x) == 7):
	        lucky += 1
	    elif (int(x) == 4):
	        lucky += 1
	if (lucky == 4):
	    ret_values.append('YES')
	elif (lucky == 7):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
