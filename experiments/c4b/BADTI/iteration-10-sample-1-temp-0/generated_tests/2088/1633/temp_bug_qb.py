def original_func(*args):
	global_list = []
	
	rows = [list(args[0]) for x in range(4)]
	
	def squarey(a, b):
	    if (rows[x][y] == rows[x][(y + b)] == rows[(x + a)][y] == rows[(x + a)][(y + b)]):
	        return True
	    else:
	        return False
	
	def squarex(a):
	    condition = False
	    if (y > 0):
	        condition = squarey(a, (- 1))
	    if ((not condition) and (y < 3)):
	        condition = squarey(a, 1)
	    return condition
	condition = False
	for x in range(4):
	    for y in range(4):
	        if (rows[x][y] == '.'):
	            rows[x][y] = '#'
	            if (x > 0):
	                condition = squarex((- 1))
	            if (not condition):
	                if (x < 3):
	                    condition = squarex(1)
	            rows[x][y] = '.'
	            if condition:
	                global_list.append('YES')
	                break
	    if condition:
	        break
	else:
	    global_list.append('NO')
	return global_list