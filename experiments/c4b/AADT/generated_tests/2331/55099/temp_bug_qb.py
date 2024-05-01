def original_func(*args):
	global_list = []
	
	(n, x_1, y_1, x_2, y_2) = [int(x) for x in args[0].split()]
	
	def normal_position_length(x_1, y_1, x_2, y_2):
	    answer0 = (abs((x_1 - x_2)) + abs((y_1 - y_2)))
	    return answer0
	
	def opposite_sides_length(n, y_1, y_2):
	    answer1 = (n + abs((y_1 - y_2)))
	    if (y_1 <= y_2):
	        answer1 += (2 * min(y_1, (n - y_2)))
	    else:
	        answer1 += (2 * min(y_2, (n - y_1)))
	    return answer1
	
	def main(n, x_1, y_1, x_2, y_2):
	    if (((x_1 + x_2) == n) and ((x_1 * x_2) == 0)):
	        return opposite_sides_length(n, y_1, y_2)
	    if (((y_1 + y_2) == n) and ((y_1 * x_2) == 0)):
	        return opposite_sides_length(n, x_1, x_2)
	    else:
	        return normal_position_length(x_1, y_1, x_2, y_2)
	global_list.append(main(n, x_1, y_1, x_2, y_2))
	return global_list