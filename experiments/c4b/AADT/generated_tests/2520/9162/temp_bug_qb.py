def original_func(*args):
	global_list = []
	
	l = args[0].split()
	n = 0
	for i in range(len(l)):
	    l[i] = int(l[i])
	    if (l[i] > n):
	        n = l[i]
	a = ((6 - n) + 1)
	if (a == 1):
	    global_list.append('1/6')
	if (a == 2):
	    global_list.append('1/3')
	if (a == 3):
	    global_list.append('1/2')
	if (a == 4):
	    global_list.append('2/3')
	if (a == 5):
	    global_list.append('5/6')
	if (a == 6):
	    global_list.append(1)
	return global_list