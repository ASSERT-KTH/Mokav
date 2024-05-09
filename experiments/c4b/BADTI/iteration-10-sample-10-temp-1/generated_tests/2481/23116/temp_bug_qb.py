def original_func(*args):
	global_list = []
	
	n = int(args[0])
	li = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	if (n <= 5):
	    global_list.append(li[(n - 1)])
	else:
	    nn = (n - 5)
	    for i in [5, 4, 3, 2, 1]:
	        if ((nn % i) == 0):
	            global_list.append(li[(i - 1)])
	            break
	return global_list