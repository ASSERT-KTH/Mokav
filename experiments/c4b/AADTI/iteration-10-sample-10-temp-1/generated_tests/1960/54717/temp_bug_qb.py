def original_func(*args):
	global_list = []
	
	row1 = args[0].split()
	global_list.append(row1)
	row2 = args[1].split()
	global_list.append(row2)
	row3 = args[2].split()
	global_list.append(row3)
	row4 = args[3].split()
	global_list.append(row4)
	row5 = args[4].split()
	global_list.append(row5)
	x = 0
	y = 0
	for i in range(5):
	    try:
	        if (i == 0):
	            y = (row1.index('1') + 1)
	            global_list.append(('found in row ' + str((i + 1))))
	            x = 1
	            break
	        elif (i == 1):
	            y = (row2.index('1') + 1)
	            global_list.append(('found in row ' + str((i + 1))))
	            x = 2
	            break
	        elif (i == 2):
	            y = (row3.index('1') + 1)
	            global_list.append(('found in row ' + str((i + 1))))
	            x = 3
	            break
	        elif (i == 3):
	            y = (row4.index('1') + 1)
	            global_list.append(('found in row ' + str((i + 1))))
	            x = 4
	            break
	        elif (i == 4):
	            y = (row5.index('1') + 1)
	            global_list.append(('found in row ' + str((i + 1))))
	            x = 5
	            break
	    except ValueError as e:
	        global_list.append('Not found')
	        pass
	global_list.append(x)
	global_list.append(y)
	xdiff = abs((3 - x))
	ydiff = abs((3 - y))
	global_list.append(xdiff)
	global_list.append(ydiff)
	moves = (xdiff + ydiff)
	global_list.append(moves)
	return global_list