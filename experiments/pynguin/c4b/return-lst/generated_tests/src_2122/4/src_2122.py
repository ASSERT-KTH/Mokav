def func(*args):
	ret_values = []
	
	row1 = args[0].split()
	row2 = args[1].split()
	row3 = args[2].split()
	row4 = args[3].split()
	row5 = args[4].split()
	x = 0
	y = 0
	for i in range(5):
	    try:
	        if (i == 0):
	            y = (row1.index('1') + 1)
	            x = 1
	            break
	        elif (i == 1):
	            y = (row2.index('1') + 1)
	            x = 2
	            break
	        elif (i == 2):
	            y = (row3.index('1') + 1)
	            x = 3
	            break
	        elif (i == 3):
	            y = (row4.index('1') + 1)
	            x = 4
	            break
	        elif (i == 4):
	            y = (row5.index('1') + 1)
	            x = 5
	            break
	    except ValueError as e:
	        pass
	xdiff = abs((3 - x))
	ydiff = abs((3 - y))
	moves = (xdiff + ydiff)
	ret_values.append(moves)

	return ret_values
