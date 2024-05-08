def original_func(*args):
	global_list = []
	
	colors = args[0].split()
	colors.sort()
	sameColor = 0
	lastColor = colors[0]
	for i in range(1, 3):
	    if (colors[i] == lastColor):
	        sameColor += 1
	    lastColor = colors[i]
	global_list.append(sameColor)
	return global_list