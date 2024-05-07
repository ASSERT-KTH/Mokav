def original_func(*args):
	global_list = []
	
	x = int(args[0])
	a = 'Sheldon'
	b = 'Leonard'
	c = 'Penny'
	d = 'Rajesh'
	e = 'Howard'
	y = (x / 5)
	if ((y % 1) != 0):
	    y = ((x // 5) + 1)
	z = 0
	i = 0
	j = 1
	lst = [0]
	while (i < x):
	    z += (5 * j)
	    i = z
	    j += 1
	    lst.append(z)
	k = lst[(len(lst) - 2)]
	zz = lst[(len(lst) - 2)]
	l = (k + 5)
	while (k < l):
	    zz += (len(lst) - 1)
	    if (x <= zz):
	        break
	    k += 1
	m = ((k + 1) % 5)
	if (m == 1):
	    global_list.append(a)
	elif (m == 2):
	    global_list.append(b)
	elif (m == 3):
	    global_list.append(c)
	elif (m == 4):
	    global_list.append(d)
	elif (m == 0):
	    global_list.append(e)
	return global_list