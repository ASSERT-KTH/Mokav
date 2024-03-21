def func(*args):
	ret_values = []
	
	ans = 0
	rawInp = args[0].split(' ')
	(a, b) = (int(rawInp[0]), int(rawInp[1]))
	while (a <= b):
	    a *= 3
	    b *= 2
	    ans += 1
	ret_values.append(ans)

	return ret_values
