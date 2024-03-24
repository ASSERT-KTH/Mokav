def func(*args):
	ret_values = []
	
	(beds, pillows, frodo) = map(int, args[0].split())
	flag = 0
	if (beds == pillows):
	    flag = 1
	pillows = ((pillows - beds) - 1)
	layer = 2
	while (pillows > 0):
	    if (beds == 1):
	        layer = (pillows + 2)
	        pillows = 0
	        break
	    if (((frodo - 1) < (layer - 1)) and ((beds - frodo) < (layer - 1))):
	        layer += (int((pillows / beds)) + 1)
	        break
	    else:
	        pillows -= (min((frodo - 1), (layer - 1)) + min((layer - 1), (beds - frodo)))
	    pillows -= 1
	    if (pillows < 0):
	        layer -= 1
	    layer += 1
	if (flag == 1):
	    ret_values.append('1')
	elif (pillows < 0):
	    ret_values.append(layer)
	elif (pillows == 0):
	    ret_values.append(layer)
	else:
	    ret_values.append((layer - 1))

	return ret_values
