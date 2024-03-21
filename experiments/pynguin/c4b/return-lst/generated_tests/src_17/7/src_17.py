def func(*args):
	ret_values = []
	
	import math
	txt = args[0]
	nums = txt.split(' ')
	l = int(nums[0])
	r = int(nums[1])
	k = int(nums[2])
	q = 1
	while (q < l):
	    q = (q * k)
	if (q > r):
	    ret_values.append('-1', end='')
	    exit()
	ret_values.append(('%d' % q), end='')
	q = (q * k)
	while (q <= r):
	    ret_values.append((' %d' % q), end='')
	    q = (q * k)

	return ret_values
