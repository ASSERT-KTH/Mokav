def original_func(*args):
	global_list = []
	
	__author__ = 'runekri3'
	movements = args[0]
	total_movements = len(movements)
	up_count = movements.count('U')
	down_count = movements.count('D')
	left_count = movements.count('L')
	right_count = movements.count('R')
	(end_x, end_y) = (0, 0)
	end_y += up_count
	end_y -= down_count
	end_x += right_count
	end_x -= left_count
	abs_x = abs(end_x)
	abs_y = abs(end_y)
	if (((abs_x == 1) and (abs_y == 0)) or ((abs_x == 0) and (abs_y == 1))):
	    if (total_movements > 1):
	        global_list.append('BUG')
	elif ((abs_x == 0) and (abs_y == 0)):
	    global_list.append('BUG')
	else:
	    last_movement = ''
	    for movement in movements:
	        if ((movement == 'U') and (last_movement == 'D')):
	            global_list.append('BUG')
	            break
	        if ((movement == 'D') and (last_movement == 'U')):
	            global_list.append('BUG')
	            break
	        if ((movement == 'L') and (last_movement == 'R')):
	            global_list.append('BUG')
	            break
	        if ((movement == 'R') and (last_movement == 'L')):
	            global_list.append('BUG')
	            break
	        last_movement = movement
	    else:
	        global_list.append('OK')
	return global_list