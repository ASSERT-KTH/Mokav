def func(*args):
	ret_values = []
	
	k = int(args[0])
	s = args[1]
	a = s.split()
	for i in range(len(a)):
	    a[i] = int(a[i])
	a.sort()
	a.reverse()
	sum = 0
	while ((k > 0) and (len(a) > 0)):
	    k -= a[0]
	    a.remove(a[0])
	    sum += 1
	if (k > 0):
	    ret_values.append((- 1))
	else:
	    ret_values.append(sum)

	return ret_values
