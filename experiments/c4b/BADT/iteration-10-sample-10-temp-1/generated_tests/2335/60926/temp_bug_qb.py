def original_func(*args):
	global_list = []
	
	lisa = args[0]
	index = ([0] * len(lisa))
	count2 = 0
	count3 = 0
	count4 = (- 1)
	count5 = 0
	mar = ([0] * len(lisa))
	for i in range(len(lisa)):
	    if (lisa[i] == 'h'):
	        count2 += 1
	    if (lisa[i] == 'e'):
	        count3 += 1
	    if (lisa[i] == 'l'):
	        count4 += 1
	        mar[count4] = i
	    if (lisa[i] == 'o'):
	        count5 += 1
	t1 = ([0] * count2)
	t2 = ([0] * count3)
	t3 = ([0] * count5)
	a1 = (- 1)
	a2 = (- 1)
	a3 = (- 1)
	if ((count2 > 0) and (count3 > 0) and (count4 > 0) and (count5 > 0)):
	    for i in range(count4):
	        a1 += 1
	        a2 += 1
	        a3 += 1
	        for j in range(mar[i], mar[(i + 1)]):
	            if (lisa[j] == 'h'):
	                t1[a1] += 1
	            if (lisa[j] == 'e'):
	                t2[a2] += 1
	            if (lisa[j] == 'o'):
	                t3[a3] += 1
	    if ((sum(t1) != count2) and (sum(t2) != count3) and (sum(t2) != count5)):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	else:
	    global_list.append('NO')
	return global_list