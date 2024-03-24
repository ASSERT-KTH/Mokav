def func(*args):
	ret_values = []
	
	import math
	n = int(args[0])
	if (n != 1):
	    ret_values.append(n, end=' ')
	flag = True
	while ((n > 1) and flag):
	    flag = False
	    for i in range(2, (int(math.sqrt(n)) + 1)):
	        if ((n % i) == 0):
	            ret_values.append((n // i), end=' ')
	            n = (n // i)
	            flag = True
	            break
	ret_values.append(1)

	return ret_values
