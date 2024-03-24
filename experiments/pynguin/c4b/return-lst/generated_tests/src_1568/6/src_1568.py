def func(*args):
	ret_values = []
	
	l1 = args[0].split(' ')
	l2 = args[1].split(' ')
	x1 = int(l1[0])
	y1 = int(l1[1])
	x2 = int(l2[0])
	y2 = int(l2[1])
	c = 0
	if ((x1 != x2) and (y1 != y2)):
	    if ((x2 > x1) and (y2 > y1)):
	        c = min((x2 - x1), (y2 - y1))
	        x2 = (x2 - c)
	        y2 = (y2 - c)
	        if (x1 != x2):
	            c = ((c + x2) - x1)
	        else:
	            c = ((c + y2) - y1)
	    elif ((x1 > x2) and (y1 > y2)):
	        c = min((x1 - x2), (y1 - y2))
	        x1 = (x1 - c)
	        y1 = (y1 - c)
	        if (x1 != x2):
	            c = ((c + x1) - x2)
	        else:
	            c = ((c + y1) - y2)
	    elif ((x1 < x2) and (y1 > y2)):
	        c = min((x2 - x1), (y1 - y2))
	        x1 = (x1 + c)
	        y1 = (y1 - c)
	        if (x1 != x2):
	            c = ((c + x2) - x1)
	        else:
	            c = ((c + y1) - y2)
	    elif ((x2 < x1) and (y2 > y1)):
	        c = min((x1 - x2), (y2 - y1))
	        x1 = (x1 - c)
	        y1 = (y1 + c)
	        if (x1 != x2):
	            c = ((c - x2) + x1)
	        else:
	            c = ((c - y1) + y2)
	elif (x1 == x2):
	    c = abs((y1 - y2))
	elif (y1 == y2):
	    c = abs((x1 - x2))
	ret_values.append(c)

	return ret_values
