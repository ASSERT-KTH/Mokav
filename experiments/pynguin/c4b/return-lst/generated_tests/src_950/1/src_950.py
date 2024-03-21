def func(*args):
	ret_values = []
	
	import math, sys, re, itertools, pprint, collections, copy
	(ri, rai) = ((lambda : int(args[0])), (lambda : list(map(int, args[1].split()))))
	(cx, c0) = (0, 0)
	a = []
	for line in sys.stdin.readlines()[:3]:
	    a.append(list(line.strip()))
	    cx += a[(- 1)].count('X')
	    c0 += a[(- 1)].count('0')
	b = []
	(s1, s2) = ('', '')
	for i in range(3):
	    s1 += a[i][i]
	    s2 += a[i][(2 - i)]
	b += [s1, s2]
	for i in range(3):
	    (s1, s2) = ('', '')
	    for j in range(3):
	        s1 += a[i][j]
	        s2 += a[j][i]
	    b += [s1, s2]
	
	def is_draw():
	    return ((cx == 5) and (c0 == 4))
	
	def is_illegal():
	    if ((not (0 <= (cx - c0) <= 1)) or (('XXX' in b) and ('000' in b))):
	        return True
	    if (('XXX' in b) and (c0 == cx)):
	        return True
	    if (('000' in b) and (cx > c0)):
	        return True
	if is_illegal():
	    ret_values.append('illegal')
	elif ('XXX' in b):
	    ret_values.append('the first player won')
	elif ('000' in b):
	    ret_values.append('the second player won')
	elif is_draw():
	    ret_values.append('draw')
	elif (cx > c0):
	    ret_values.append('second')
	else:
	    ret_values.append('first')

	return ret_values
