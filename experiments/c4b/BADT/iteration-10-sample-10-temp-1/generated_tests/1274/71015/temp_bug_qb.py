def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	if ((k == 1) or (l == 1) or (m == 1) or (n == 1)):
	    global_list.append(d)
	elif ((k > d) and (l > d) and (m > d) and (n > d)):
	    global_list.append(0)
	else:
	    from math import sqrt
	    n = d
	    lst = []
	    for i in range(2, (n + 1)):
	        if (i > 10):
	            if (((i % 2) == 0) or ((i % 10) == 5)):
	                continue
	        for j in lst:
	            if ((j > int((sqrt(i) + 1))) and (j != k) and (j != l) and (j != m) and (j != n) and (j != d)):
	                lst.append(i)
	                break
	            if ((i % j) == 0):
	                break
	        else:
	            lst.append(i)
	    count = len(lst)
	    i = 0
	    lenght = 0
	    while (count > 0):
	        if ((lst[i] != k) and (lst[i] != l) and (lst[i] != m) and (lst[i] != n)):
	            lenght += 1
	        i += 1
	        count -= 1
	    global_list.append((d - lenght))
	return global_list