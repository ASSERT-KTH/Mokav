def original_func(*args):
	global_list = []
	
	d_min = 0
	x = args[0]
	x += '$'
	start = 0
	z = []
	while (start != (len(x) - 1)):
	    if (x[start] in 'AEIOUY'):
	        y = x[start]
	        start += 1
	        while (start != (len(x) - 1)):
	            if (x[start] not in 'AEIOUY'):
	                y += x[start]
	                start += 1
	            else:
	                break
	        z.append(y)
	        if (d_min < len(y)):
	            d_min = len(y)
	    else:
	        start += 1
	if (z == []):
	    global_list.append(len(x))
	else:
	    global_list.append(d_min)
	return global_list