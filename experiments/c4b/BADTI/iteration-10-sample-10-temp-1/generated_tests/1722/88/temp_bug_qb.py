def original_func(*args):
	global_list = []
	
	a = int(args[0])
	x = 0
	div = []
	for i in range(1, (int((a ** 0.5)) + 1)):
	    if ((a % i) == 0):
	        div.append(i)
	for i in div:
	    t = 0
	    for j in str(i):
	        if (j in str(a)):
	            t = 1
	    x += t
	x += 1
	if (a == 1):
	    x -= 1
	global_list.append(x)
	return global_list