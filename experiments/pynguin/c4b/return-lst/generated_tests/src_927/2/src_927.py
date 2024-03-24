def func(*args):
	ret_values = []
	
	(y, k, n) = map(int, args[0].split())
	temp = int((y / k))
	temp += 1
	temp = (temp * k)
	if (temp > n):
	    ret_values.append((- 1))
	    exit()
	while (temp <= n):
	    ret_values.append((temp - y), end=' ')
	    temp += k
	ret_values.append()

	return ret_values
