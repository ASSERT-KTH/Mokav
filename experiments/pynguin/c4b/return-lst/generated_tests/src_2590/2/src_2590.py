def func(*args):
	ret_values = []
	
	n = int(args[0])
	ans = ''
	if ((n % 2) == 0):
	    for i in range((n // 2)):
	        ans += '1'
	else:
	    ans += '7'
	    for i in range(((n // 2) - 1)):
	        ans += '1'
	ret_values.append(ans)

	return ret_values
