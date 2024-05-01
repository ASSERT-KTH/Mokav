def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	count = 0
	five = int((n / 5))
	if (five > 0):
	    n -= (five * 5)
	    count += five
	four = int((n / 4))
	if (four > 0):
	    n -= (four * 4)
	    count += four
	three = int((n / 3))
	if (three > 0):
	    n -= (three * 3)
	    count += three
	two = int((n / 2))
	if (two > 0):
	    n -= (two * 2)
	    count += two
	one = int((n / 1))
	if (one > 0):
	    n -= (one * 4)
	    count += one
	global_list.append(count)
	return global_list