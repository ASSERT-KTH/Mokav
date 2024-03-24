def func(*args):
	ret_values = []
	
	n = int(args[0])
	ans = ''
	for i in range(32, (- 1), (- 1)):
	    if ((n & (1 << i)) is not 0):
	        ans += str((i + 1))
	        ans += ' '
	ret_values.append(ans)

	return ret_values
