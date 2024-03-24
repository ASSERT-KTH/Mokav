def func(*args):
	ret_values = []
	
	(h, m) = args[0].split(':')
	h = int(h)
	m = int(m)
	L = [0, 1.1, 2.2, 3.3, 4.4, 5.5, 10.01, 11.11, 12.21, 13.31, 14.41, 15.51, 20.02, 21.12, 22.22, 23.32]
	a = (h + (0.01 * m))
	if (L.count(a) == 0):
	    L.append(a)
	L.sort()
	if (L.index(a) < (len(L) - 1)):
	    s = str(L[(L.index(a) + 1)])
	    L1 = s.split('.')
	    if (len(L1[0]) == 1):
	        h1 = ('0' + L1[0])
	        L1[0] = h1
	    if (len(L1[1]) == 1):
	        m1 = (L1[1] + '0')
	        L1[1] = m1
	    r = ((L1[0] + ':') + L1[1])
	else:
	    r = '00:00'
	ret_values.append(r)

	return ret_values
