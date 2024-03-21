def func(*args):
	ret_values = []
	
	l1 = args[0]
	l2 = args[1]
	l3 = args[2]
	l4 = args[3]
	l5 = args[4]
	l6 = args[5]
	l7 = args[6]
	l8 = args[7]
	d = []
	c = 0
	if (l1.count('B') == 8):
	    c += 1
	else:
	    d += [l1.count('B')]
	if (l2.count('B') == 8):
	    c += 1
	else:
	    d += [l2.count('B')]
	if (l3.count('B') == 8):
	    c += 1
	else:
	    d += [l3.count('B')]
	if (l4.count('B') == 8):
	    c += 1
	else:
	    d += [l4.count('B')]
	if (l5.count('B') == 8):
	    c += 1
	else:
	    d += [l5.count('B')]
	if (l6.count('B') == 8):
	    c += 1
	else:
	    d += [l6.count('B')]
	if (l7.count('B') == 8):
	    c += 1
	else:
	    d += [l7.count('B')]
	if (l8.count('B') == 8):
	    c += 1
	else:
	    d += [l8.count('B')]
	r = 0
	if (len(d) >= 1):
	    r = max(d)
	ret_values.append((c + r))

	return ret_values
