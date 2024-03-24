def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	total_time = 240
	remaining_time = (total_time - k)
	result = 0
	for i in range(1, (n + 1), 1):
	    if ((remaining_time - (5 * i)) >= 0):
	        remaining_time -= (5 * i)
	        result += 1
	    else:
	        break
	ret_values.append(result)

	return ret_values
