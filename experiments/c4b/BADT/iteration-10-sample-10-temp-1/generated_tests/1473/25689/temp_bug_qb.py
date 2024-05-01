def original_func(*args):
	global_list = []
	
	from math import sqrt
	
	def right(x1, y1, x2, y2, x3, y3):
	    d1s = (((y2 - y1) ** 2) + ((x2 - x1) ** 2))
	    d2s = (((y3 - y2) ** 2) + ((x3 - x2) ** 2))
	    d3s = (((y1 - y3) ** 2) + ((x1 - x3) ** 2))
	    (a, b, c) = sorted([d1s, d2s, d3s])
	    return (c == (a + b))
	(x1, y1, x2, y2, x3, y3) = map(int, args[0].split())
	if right(x1, y1, x2, y2, x3, y3):
	    global_list.append('RIGHT')
	elif (right((x1 - 1), y1, x2, y2, x3, y3) or right((x1 + 1), y1, x2, y2, x3, y3) or right(x1, (y1 - 1), x2, y2, x3, y3) or right(x1, (y1 + 1), x2, y2, x3, y3) or right(x1, y1, (x2 - 1), y2, x3, y3) or right(x1, y1, (x2 + 1), y2, x3, y3) or right(x1, y1, x2, (y2 - 1), x3, y3) or right(x1, y1, x2, (y2 + 1), x3, y3) or right(x1, y1, x2, y2, (x3 - 1), y3) or right(x1, y1, x2, y2, (x3 + 1), y3) or right(x1, y1, x2, y2, x3, (y3 - 1)) or right(x1, y1, x2, y2, x3, (y3 + 1))):
	    global_list.append('ALMOST')
	else:
	    global_list.append('NEITHER')
	return global_list