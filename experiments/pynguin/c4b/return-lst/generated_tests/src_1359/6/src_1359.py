def func(*args):
	ret_values = []
	
	x = args[0]
	
	def limites():
	    pos = 8
	    if ((x[1] == '1') or (x[1] == '8')):
	        pos -= 3
	    if ((x[0] == 'a') or (x[0] == 'h')):
	        pos -= 3
	    if (pos == 2):
	        pos += 1
	    return pos
	ret_values.append(limites())

	return ret_values
