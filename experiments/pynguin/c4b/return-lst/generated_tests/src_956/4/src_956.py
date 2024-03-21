def func(*args):
	ret_values = []
	
	(n, k) = args[0].split()
	n = int(n)
	k = int(k)
	sum = 0
	if (n == 1):
	    ret_values.append(sum)
	elif (n == 2):
	    sum = 1
	    ret_values.append(sum)
	else:
	    for i in range(k):
	        sum += ((2 * n) - 3)
	        n -= 2
	        if (n < 2):
	            break
	    ret_values.append(sum)

	return ret_values
