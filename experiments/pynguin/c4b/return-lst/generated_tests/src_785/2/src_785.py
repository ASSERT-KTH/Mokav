def func(*args):
	ret_values = []
	
	import sys
	permSize = int(args[0])
	if ((permSize % 2) == 1):
	    ret_values.append('-1')
	    sys.exit()
	odd = 1
	even = 2
	for i in range(permSize):
	    if ((i % 2) == 0):
	        ret_values.append(even, end=' ')
	        even += 2
	    else:
	        ret_values.append(odd, end=' ')
	        odd += 2

	return ret_values
