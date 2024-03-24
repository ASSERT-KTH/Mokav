def func(*args):
	ret_values = []
	
	n = int(args[0])
	sum = 0
	s = 1
	while (int(bin(s)[2:]) <= n):
	    sum += 1
	    s += 1
	ret_values.append(sum)

	return ret_values
