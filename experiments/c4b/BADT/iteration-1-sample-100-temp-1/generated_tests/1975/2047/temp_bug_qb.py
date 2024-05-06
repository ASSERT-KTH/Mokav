def original_func(*args):
	global_list = []
	
	x = args[0].split()
	a = int(x[0])
	b = int(x[1])
	y = args[1]
	yy = list(y)
	i = 0
	while (i < b):
	    j = 0
	    while (j < (len(yy) - 1)):
	        if (((j + 1) < len(yy)) and (yy[j] == 'B') and (yy[(j + 1)] == 'G')):
	            tmp = yy[j]
	            yy[j] = yy[(j + 1)]
	            yy[(j + 1)] = tmp
	            j += 1
	        j += 1
	    i += 1
	z = ''.join(yy)
	global_list.append(y)
	return global_list