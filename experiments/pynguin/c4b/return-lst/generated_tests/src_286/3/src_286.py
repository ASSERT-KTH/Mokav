def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = list(map(int, args[1].split()))
	a.sort(reverse=True)
	d = 0
	m = 0
	for i in range(12):
	    d += a[i]
	    m += 1
	    if (d >= k):
	        break
	if (k == 0):
	    ret_values.append('0')
	elif (d < k):
	    ret_values.append('-1')
	else:
	    ret_values.append(m)

	return ret_values
