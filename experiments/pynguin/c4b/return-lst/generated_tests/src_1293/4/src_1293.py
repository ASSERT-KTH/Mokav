def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = args[1]
	b = list(map(int, a.split()))
	b.sort()
	sum = 0
	if (k == 0):
	    ret_values.append(0)
	else:
	    for i in range(12):
	        sum = (sum + b[(11 - i)])
	        if (sum >= k):
	            ret_values.append((i + 1))
	            break
	        if ((sum < k) and (i == 11)):
	            ret_values.append((- 1))

	return ret_values
