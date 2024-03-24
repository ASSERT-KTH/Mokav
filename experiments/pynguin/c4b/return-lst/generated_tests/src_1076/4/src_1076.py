def func(*args):
	ret_values = []
	
	(m, b) = map(int, args[0].split())
	ans = 0
	for y in range(0, (b + 1)):
	    x = (m * (b - y))
	    ans = max(ans, (((x + 1) * ((y * (y + 1)) // 2)) + ((y + 1) * ((x * (x + 1)) // 2))))
	ret_values.append(ans)

	return ret_values
