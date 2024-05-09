def patched_func(*args):
	global_list = []
	
	import math
	
	def vectorLength(x1, y1, x2, y2):
	    return math.sqrt((math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2)))
	(xa, ya) = [int(item) for item in args[0].split()]
	(xb, yb) = [int(item) for item in args[1].split()]
	(xc, yc) = [int(item) for item in args[2].split()]
	if (round((vectorLength(xa, ya, xb, yb) + vectorLength(xb, yb, xc, yc))) == round(vectorLength(xa, ya, xc, yc))):
	    global_list.append('TOWARDS')
	elif (((ya < yb) and (xc > xb)) or ((ya > yb) and (xc < xb)) or ((ya == yb) and (yc < yb) and (xb > xa)) or ((ya == yb) and (yc > yb) and (xb < xa))):
	    global_list.append('RIGHT')
	else:
	    global_list.append('LEFT')
	return global_list