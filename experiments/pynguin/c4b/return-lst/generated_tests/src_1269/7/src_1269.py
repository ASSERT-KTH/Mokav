def func(*args):
	ret_values = []
	
	m = int(args[0])
	reg = args[1].split()
	counter = 0
	sum1 = 0
	i = 0
	while (sum1 < m):
	    sum1 += int(reg[(i % 7)])
	    counter += 1
	    i += 1
	ret_values.append((((counter - 1) % 7) + 1))

	return ret_values
