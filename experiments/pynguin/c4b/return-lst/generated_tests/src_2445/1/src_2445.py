def func(*args):
	ret_values = []
	
	colors = args[0].split()
	colors.sort()
	sameColor = 0
	lastColor = ''
	for i in range(4):
	    if (colors[i] == lastColor):
	        sameColor += 1
	    lastColor = colors[i]
	ret_values.append(sameColor)

	return ret_values
