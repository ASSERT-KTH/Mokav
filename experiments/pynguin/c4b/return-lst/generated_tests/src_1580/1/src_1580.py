def func(*args):
	ret_values = []
	
	n = int(args[0])
	ans = ''
	if ((n % 2) == 0):
	    ans = (ans + ('1' * (n // 2)))
	elif (n == 3):
	    ans = '7'
	else:
	    n -= 3
	    ans = (ans + '7')
	    ans = (ans + ('1' * (n // 2)))
	ret_values.append(ans)

	return ret_values
