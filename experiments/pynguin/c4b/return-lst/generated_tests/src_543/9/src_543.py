def func(*args):
	ret_values = []
	
	import sys
	n = int(args[0])
	x = list(map(int, args[1].split()))
	x = sorted(x, reverse=True)
	count = 0
	sum = 0
	if (sum < n):
	    for i in range(len(x)):
	        sum += x[i]
	        if (sum >= n):
	            ret_values.append((i + 1))
	            sys.exit()
	    ret_values.append((- 1))
	    sys.exit()
	ret_values.append(0)

	return ret_values
