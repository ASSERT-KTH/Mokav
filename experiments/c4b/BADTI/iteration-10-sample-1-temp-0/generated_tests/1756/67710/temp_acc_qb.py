def patched_func(*args):
	global_list = []
	
	colors = args[0].split()
	colors.sort()
	sameColor = 0
	lastColor = ''
	for i in range(4):
	    if (colors[i] == lastColor):
	        sameColor += 1
	    lastColor = colors[i]
	global_list.append(sameColor)
	return global_list