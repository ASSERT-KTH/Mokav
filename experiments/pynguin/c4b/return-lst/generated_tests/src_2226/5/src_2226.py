def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	damaged_dragons = 0
	for i in range(1, (d + 1)):
	    if (((i % k) == 0) or ((i % l) == 0) or ((i % m) == 0) or ((i % n) == 0)):
	        damaged_dragons += 1
	    else:
	        None
	ret_values.append(damaged_dragons)

	return ret_values
