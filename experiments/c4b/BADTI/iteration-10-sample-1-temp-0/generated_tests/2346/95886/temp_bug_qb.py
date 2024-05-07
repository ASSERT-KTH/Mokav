def original_func(*args):
	global_list = []
	
	
	def build_triangle(sides):
	    (a, b, c, d) = sides
	    if (((a + b) > c) and ((a + c) > b) and ((c + b) > a)):
	        global_list.append('TRIANGLE')
	    elif (((a + c) > d) and ((a + d) > c) and ((c + d) > a)):
	        global_list.append('TRIANGLE')
	    elif (((b + c) > d) and ((b + d) > c) and ((c + d) > b)):
	        global_list.append('TRIANGLE')
	    elif (((a + d) > b) and ((a + b) > d) and ((b + d) > a)):
	        global_list.append('TRIANGLE')
	    elif (((a + b) == c) or ((a + c) == b) or ((c + b) == a)):
	        global_list.append('SEGMENT')
	    elif (((a + c) == d) or ((a + d) == c) or ((c + d) == a)):
	        global_list.append('SEGMENT')
	    elif (((b + c) == d) or ((b + d) == c) or ((c + d) == b)):
	        global_list.append('SEGMENT')
	    elif (((a + d) == b) or ((a + b) == d) or ((b + d) == a)):
	        global_list.append('SEGMENT')
	    else:
	        global_list.append('IMPOSSIBLE')
	return global_list