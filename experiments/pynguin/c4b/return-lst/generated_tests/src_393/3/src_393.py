def func(*args):
	ret_values = []
	
	rows = [args[0] for x in range(4)]
	(columns, d1, d2, d3, d4, d5, d6) = ([''.join([x[y] for x in rows]) for y in range(4)], ''.join([rows[x][x] for x in range(4)]), ''.join([rows[x][(3 - x)] for x in range(4)]), ''.join([rows[x][(2 - x)] for x in range(3)]), ''.join([rows[x][(x + 1)] for x in range(3)]), ''.join([rows[x][(x - 1)] for x in range(1, 4)]), ''.join([rows[x][(4 - x)] for x in range(1, 4)]))
	diagonals = [d1, d2, d3, d4, d5, d6]
	lines = ((rows + columns) + diagonals)
	for x in lines:
	    y = x.replace('o', ' ')
	    if (('x.x' in y) or ('xx.' in y) or ('.xx' in y)):
	        ret_values.append('YES')
	        break
	else:
	    ret_values.append('NO')

	return ret_values
