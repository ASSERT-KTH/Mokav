def func(*args):
	ret_values = []
	
	n = int(args[0])
	if ((n % 2) == 1):
	    ret_values.append('7', end='')
	    n = (n - 3)
	for i in range((n // 2)):
	    ret_values.append('1', end='')

	return ret_values
