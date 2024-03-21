def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	sum = 0
	for i in range(1, (n + 1)):
	    sum = (sum + ((m + (i % 5)) // 5))
	ret_values.append(sum)

	return ret_values
