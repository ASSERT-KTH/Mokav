def func(*args):
	
	X = args[0]
	l = []
	k = ''
	for i in X:
	    if (i == ' '):
	        l.append(int(k))
	        k = ''
	        continue
	    k = (k + i)
	l.append(int(k))
	if ((l[0] % l[2]) != 0):
	    a = ((l[0] // l[2]) + 1)
	else:
	    a = (l[0] // l[2])
	if ((l[1] % l[2]) != 0):
	    b = ((l[1] // l[2]) + 1)
	else:
	    b = (l[1] // l[2])
	return((a * b))
