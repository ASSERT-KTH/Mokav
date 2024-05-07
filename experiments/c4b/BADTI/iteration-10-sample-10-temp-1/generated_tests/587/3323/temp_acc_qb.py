def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	digits = args[1]
	pos = []
	for c in digits:
	    first_digit = int(c)
	    if (first_digit == 0):
	        start_pos = (3, 1)
	    else:
	        start_pos = (((first_digit - 1) // 3), ((first_digit - 1) % 3))
	    pos.append(start_pos)
	if (((3, 1) in pos) and (((0, 0) in pos) or ((0, 1) in pos) or ((0, 2) in pos))):
	    global_list.append('YES')
	else:
	    maxX = 0
	    minX = 2
	    maxY = 0
	    minY = 2
	    for (x, y) in pos:
	        maxX = max(x, maxX)
	        minX = min(x, minX)
	        maxY = max(y, maxY)
	        minY = min(y, minY)
	    if ((minX == 0) and (maxX == 2) and (minY == 0) and (maxY == 2)):
	        if (((2, 2) not in pos) and ((2, 0) not in pos)):
	            global_list.append('NO')
	        else:
	            global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list