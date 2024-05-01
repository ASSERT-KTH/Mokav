def original_func(*args):
	global_list = []
	
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
	    for i in range(0, len(n)):
	        if (i < (len(n) // 2)):
	            a.append(n[i])
	        else:
	            b.append(n[i])
	        for i in a:
	            suma += int(i)
	        for i in b:
	            sumb += int(i)
	        if (suma == sumb):
	            global_list.append('YES')
	        else:
	            global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list