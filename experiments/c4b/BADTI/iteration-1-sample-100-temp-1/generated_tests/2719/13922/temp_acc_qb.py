def patched_func(*args):
	global_list = []
	
	str = args[0].split()
	a = int(str[0])
	b = int(str[1])
	count = 0
	if (a == b):
	    global_list.append('1')
	else:
	    while (a <= b):
	        a = (a * 3)
	        b = (b * 2)
	        count += 1
	    global_list.append(count)
	return global_list