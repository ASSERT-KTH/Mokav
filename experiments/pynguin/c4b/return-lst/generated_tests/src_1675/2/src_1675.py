def func(*args):
	ret_values = []
	
	n = int(args[0])
	x = (n // 4)
	y = ((n // 7) + 1)
	flag = False
	for i in range(0, (x + 1)):
	    if (flag == True):
	        break
	    for j in range(0, (y + 1)):
	        if (((i * 4) + (j * 7)) == n):
	            s = ((i * '4') + (j * '7'))
	            flag = True
	            ret_values.append(s)
	            break
	if (flag == False):
	    ret_values.append('-1')

	return ret_values
