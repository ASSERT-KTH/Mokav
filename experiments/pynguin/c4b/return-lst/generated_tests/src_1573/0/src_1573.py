def func(*args):
	ret_values = []
	
	a = args[0]
	s = 0
	d = []
	d1 = []
	f = 0
	ff = 0
	p = []
	for i in range(len(a)):
	    if (i != (len(a) - 1)):
	        if ((a[i] + a[(i + 1)]) == 'VK'):
	            s = (s + 1)
	            d.append((i + 1))
	            d1.append(i)
	for i in range(len(a)):
	    if (i != (len(a) - 1)):
	        if ((((a[i] + a[(i + 1)]) == 'KK') and (i not in d)) or (((a[i] + a[(i + 1)]) == 'VV') and ((i + 1) not in d1))):
	            s = (s + 1)
	            break
	if (len(a) != 1):
	    ret_values.append(s)
	else:
	    ret_values.append(0)

	return ret_values
