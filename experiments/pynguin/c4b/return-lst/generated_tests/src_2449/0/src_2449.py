def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = [int(i) for i in args[1].split()]
	if (k == 0):
	    ret_values.append('0')
	else:
	    a.sort(reverse=True)
	    for i in range(12):
	        if (sum(a[0:(i + 1)]) >= k):
	            ret_values.append((i + 1))
	            break
	    else:
	        ret_values.append('-1')

	return ret_values
