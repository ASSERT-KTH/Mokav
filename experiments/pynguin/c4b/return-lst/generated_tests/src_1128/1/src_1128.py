def func(*args):
	ret_values = []
	
	import sys
	arr = list(map(int, args[0].split()))
	l1 = arr[0]
	r1 = arr[1]
	l2 = arr[2]
	r2 = arr[3]
	k = arr[4]
	cnt = 0
	a = max(l1, l2)
	b = min(r1, r2)
	if (a > b):
	    ret_values.append(0)
	elif ((a <= k) and (k <= b)):
	    ret_values.append((b - a))
	else:
	    ret_values.append(((b - a) + 1))

	return ret_values
