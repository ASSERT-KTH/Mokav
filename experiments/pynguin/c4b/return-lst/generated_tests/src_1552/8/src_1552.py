def func(*args):
	ret_values = []
	
	s = args[0]
	a = []
	a = s.split()
	for i in range(len(a)):
	    a[i] = int(a[i])
	b = []
	i = 1
	while ((a[1] * i) <= a[2]):
	    if ((a[1] * i) > a[0]):
	        b.append(((a[1] * i) - a[0]))
	    i += 1
	if (len(b) == 0):
	    ret_values.append((- 1))
	else:
	    for i in range(len(b)):
	        ret_values.append(b[i], end=' ')

	return ret_values
