def func(*args):
	ret_values = []
	
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
	
	def check():
	    condition = False
	    if (x > 0):
	        condition = squarex((- 1))
	    if (not condition):
	        if (x < 3):
	            condition = squarex(1)
	    return condition
	condition = False
	for x in range(4):
	    for y in range(4):
	        condition = check()
	        if (not condition):
	            r = rows[x][y]
	            if (r == '#'):
	                rows[x][y] = '.'
	                condition = check()
	                rows[x][y] = '#'
	            else:
	                rows[x][y] = '#'
	                condition = check()
	                rows[x][y] = '.'
	        if condition:
	            ret_values.append('YES')
	            break
	    if condition:
	        break
	else:
	    ret_values.append('NO')

	return ret_values
