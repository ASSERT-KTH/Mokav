def patched_func(*args):
	global_list = []
	
	'\nCF problem 228A\n@autor Yergali B\n'
	a = sorted(list(map(int, args[0].split())))
	b = []
	c = 0
	for i in range(4):
	    for j in range(4):
	        if (a[i] != a[j]):
	            c += 1
	    b.append(c)
	    c = 0
	if (max(a) == min(a)):
	    global_list.append(3)
	elif (max(b) == min(b) == 2):
	    global_list.append(2)
	else:
	    global_list.append((3 - min(b)))
	return global_list