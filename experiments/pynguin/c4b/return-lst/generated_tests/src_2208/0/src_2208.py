def func(*args):
	ret_values = []
	
	ans = 0
	(n, m) = map(int, args[0].split())
	for i in range((n + 1)):
	    for j in range((m + 1)):
	        if ((((i * i) + j) == n) and (((j * j) + i) == m)):
	            ans += 1
	ret_values.append(('%d' % ans))

	return ret_values
