def original_func(*args):
	global_list = []
	
	a = args[0]
	(x, y) = a.split(':')
	x1 = x[::(- 1)]
	if ((x == '23') and (int(y) >= 32)):
	    global_list.append('00:00')
	elif (int(x1) > int(y)):
	    while (int(x1) >= 60):
	        x = int(x)
	        x += 1
	        if (len(str(x)) == 1):
	            x1 = ('0' + str(x))[::(- 1)]
	        else:
	            x1 = str(x)[::(- 1)]
	    if (len(str(x)) == 2):
	        global_list.append(((str(x) + ':') + str(x1)))
	    else:
	        global_list.append(((('0' + str(x)) + ':') + str(x1)))
	else:
	    x2 = str((int(x) + 1))
	    y2 = x2[::(- 1)]
	    while (int(y2) >= 60):
	        x2 = int(x2)
	        y2 = int(y2)
	        x2 += 1
	        y2 = str(x2)[::(- 1)]
	    global_list.append(((str(x2) + ':') + y2))
	return global_list