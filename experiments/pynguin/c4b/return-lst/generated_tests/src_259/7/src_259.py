def func(*args):
	ret_values = []
	
	k = int(args[0])
	a = list(map(int, args[1].split()))
	a.sort(reverse=True)
	c = 0
	f = 0
	for i in range(12):
	    if (c < k):
	        c += a[i]
	        f += 1
	    if (c >= k):
	        break
	if (c >= k):
	    ret_values.append(f)
	else:
	    ret_values.append((- 1))

	return ret_values
