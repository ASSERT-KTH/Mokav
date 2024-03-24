def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	if (a > b):
	    (a, b) = (b, a)
	ans = 1
	for i in range(2, (a + 1)):
	    ans *= i
	ret_values.append(ans)

	return ret_values
