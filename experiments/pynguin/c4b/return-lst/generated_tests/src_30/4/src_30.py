def func(*args):
	ret_values = []
	
	(l1, r1, l2, r2, k) = map(int, args[0].split())
	if ((l2 > r1) or (l1 > r2)):
	    ret_values.append(0)
	elif ((l2 >= l1) and (r2 <= r1)):
	    ret_values.append((((r2 - l2) + 1) - ((k >= l2) and (k <= r2))))
	elif ((l1 >= l2) and (r1 <= r2)):
	    ret_values.append((((r1 - l1) + 1) - ((k >= l1) and (k <= r1))))
	elif (l2 >= l1):
	    ret_values.append((((r1 - l2) + 1) - ((k >= l2) and (k <= r1))))
	elif (l1 >= l2):
	    ret_values.append((((r2 - l1) + 1) - ((k >= l1) and (k <= r2))))

	return ret_values
