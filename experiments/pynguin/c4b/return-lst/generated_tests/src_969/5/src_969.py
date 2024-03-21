def func(*args):
	ret_values = []
	
	n = int(args[0])
	(f, s) = ((n // 7), 0)
	ans = (- 1)
	for i in range(f, (- 1), (- 1)):
	    if (((n - (7 * i)) % 4) == 0):
	        ans = i
	        break
	if (ans == (- 1)):
	    ret_values.append((- 1))
	else:
	    ret_values.append((('4' * ((n - (7 * ans)) // 4)) + ('7' * ans)))

	return ret_values
