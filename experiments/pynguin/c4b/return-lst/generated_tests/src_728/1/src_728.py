def func(*args):
	ret_values = []
	
	n = int(args[0])
	bindigits = []
	start = 0
	while (n > 0):
	    bindigits.insert(0, (n % 2))
	    n = (n // 2)
	    start += 1
	for bit in bindigits:
	    if (bit == 1):
	        ret_values.append(start, end=' ')
	    start -= 1

	return ret_values
