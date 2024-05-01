def original_func(*args):
	global_list = []
	
	(x, y, z, k) = map(int, args[0].split())
	a = [x, y, z]
	if (x == y == z == 1):
	    global_list.append(1)
	if ((x == y == 1) and (z > 1)):
	    global_list.append(z)
	if ((x == 1) and (y > 1) and (z > 1)):
	    global_list.append((y * z))
	while ((x > 1) and (y > 1) and (z > 1)):
	    if (k == 1):
	        global_list.append(2)
	    if (k == 2):
	        global_list.append(4)
	    if (k == 3):
	        global_list.append(8)
	    if (k > (((x - 1) + (y - 1)) + (z - 1))):
	        global_list.append(((x * y) * z))
	    if (3 < k <= (((x - 1) + (y - 1)) + (z - 1))):
	        global_list.append(((4 * k) - 4))
	    break
	return global_list