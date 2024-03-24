def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split()))
	if ((a[0] > 1) & (a[1] == 1)):
	    ret_values.append((- 1))
	elif (a[0] == a[1] == 1):
	    ret_values.append('a')
	elif (a[1] > a[0]):
	    ret_values.append((- 1))
	else:
	    ret_values.append(((('ab' * (((a[0] + 2) - a[1]) // 2)) + ('a' * ((a[0] - a[1]) % 2))) + ''.join(map((lambda x: chr((ord('c') + x))), range((a[1] - 2))))))

	return ret_values
