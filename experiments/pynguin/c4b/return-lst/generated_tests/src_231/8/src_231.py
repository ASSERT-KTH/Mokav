def func(*args):
	ret_values = []
	
	(n, k) = list(map(int, args[0].split()))
	l = [(i * 5) for i in range(1, (n + 1))]
	count = 0
	for i in range(n):
	    if (sum(l[:(i + 1)]) > (240 - k)):
	        break
	    count += 1
	ret_values.append(count)

	return ret_values
