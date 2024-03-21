def func(*args):
	ret_values = []
	
	__author__ = 'runekri3'
	
	def cells_touching(cell_1, cell_2):
	    abs_x = abs((cell_1[0] - cell_2[0]))
	    if (abs_x > 1):
	        return False
	    abs_y = abs((cell_1[1] - cell_2[1]))
	    if (abs_y > 1):
	        return False
	    if (not ((abs_x == 1) and (abs_y == 1))):
	        return True
	movements = args[0]
	total_movements = len(movements)
	cur_cell = [0, 0]
	visited_cells = [(0, 0)]
	last_movement = ''
	bug = False
	for movement in movements:
	    if (movement == 'U'):
	        cur_cell[1] += 1
	    elif (movement == 'D'):
	        cur_cell[1] -= 1
	    elif (movement == 'R'):
	        cur_cell[0] += 1
	    else:
	        cur_cell[0] -= 1
	    for visited_cell in visited_cells[:(- 1)]:
	        if cells_touching(cur_cell, visited_cell):
	            bug = True
	            break
	    visited_cells.append(tuple(cur_cell))
	if bug:
	    ret_values.append('BUG')
	else:
	    ret_values.append('OK')

	return ret_values
