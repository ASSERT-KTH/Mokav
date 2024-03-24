def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	ans = 0
	while (a <= b):
	    a *= 3
	    b *= 2
	    ans += 1
	ret_values.append(ans)

	return ret_values
