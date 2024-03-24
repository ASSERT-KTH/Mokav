def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = list(map(int, args[1].split()))
	a.sort()
	if (n % 2):
	    ret_values.append(a[(n // 2)])

	return ret_values
