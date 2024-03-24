def func(*args):
	ret_values = []
	
	n = int(args[0])
	n = list(args[1])
	a = []
	b = []
	suma = 0
	sumb = 0
	c = 0
	for i in n:
	    i = int(i)
	    if (i == 4):
	        c += 0
	    elif (i == 7):
	        c += 0
	    else:
	        c += 1
	if (c == 0):
	    for i in n:
	        if (len(a) < (len(n) // 2)):
	            a.append(i)
	        else:
	            b.append(i)
	    for i in a:
	        suma += int(i)
	    for i in b:
	        sumb += int(i)
	    if (suma == sumb):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif (c > 0):
	    ret_values.append('NO')

	return ret_values
